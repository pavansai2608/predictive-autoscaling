"use client";

import { RUN_SECONDS } from "@/lib/data";

export interface ChartSeries {
  label: string;
  colour: string;
  /** SVG stroke-dasharray. Series are keyed by dash AND colour AND a direct
   *  label, because the three arm colours do not separate under deuteranopia. */
  dashArray?: string;
  points: { t: number; v: number | null }[];
}

interface Props {
  title: string;
  unit: string;
  series: ChartSeries[];
  /** Draw only up to here, so dragging the playhead replays the run. */
  playhead: number;
  /** [start, end] of the load event in seconds, read off the k6 stage list. */
  event: [number, number];
  height?: number;
  /** Step-after interpolation for pod counts — replicas change discretely. */
  step?: boolean;
}

const W = 760;
const PAD = { top: 14, right: 96, bottom: 30, left: 46 };

/**
 * Hand-rolled SVG rather than a charting library: the whole chart is four
 * paths and some text, and every library considered ships its own theme that
 * would fight the report styling. Bundle cost here is zero.
 */
export default function Chart({ title, unit, series, playhead, event, height = 220, step = false }: Props) {
  const H = height;
  const iw = W - PAD.left - PAD.right;
  const ih = H - PAD.top - PAD.bottom;

  // The y-axis is scaled to the WHOLE run, never to what has been drawn yet.
  // A y-axis that grows as you scrub makes an early spike look identical to a
  // late one, and the panel would resize on every slider tick.
  const allValues = series.flatMap((s) => s.points.map((p) => p.v)).filter((v): v is number => v !== null);
  const yMax = allValues.length ? Math.max(...allValues) * 1.08 : 1;

  const x = (t: number) => PAD.left + (t / RUN_SECONDS) * iw;
  const y = (v: number) => PAD.top + ih - (v / yMax) * ih;

  const yTicks = 4;
  const xTicks = 6;

  const pathFor = (s: ChartSeries) => {
    const pts = s.points.filter((p) => p.t <= playhead && p.v !== null) as { t: number; v: number }[];
    if (pts.length === 0) return "";
    let d = `M ${x(pts[0].t).toFixed(1)} ${y(pts[0].v).toFixed(1)}`;
    for (let i = 1; i < pts.length; i++) {
      if (step) d += ` H ${x(pts[i].t).toFixed(1)} V ${y(pts[i].v).toFixed(1)}`;
      else d += ` L ${x(pts[i].t).toFixed(1)} ${y(pts[i].v).toFixed(1)}`;
    }
    return d;
  };

  const lastPoint = (s: ChartSeries) => {
    const pts = s.points.filter((p) => p.t <= playhead && p.v !== null) as { t: number; v: number }[];
    return pts.length ? pts[pts.length - 1] : null;
  };

  // Direct labels are stacked apart when two series end at nearly the same
  // height, otherwise they overprint and the keying is lost.
  const labels = series
    .map((s) => ({ s, p: lastPoint(s) }))
    .filter((o): o is { s: ChartSeries; p: { t: number; v: number } } => o.p !== null)
    .sort((a, b) => a.p.v - b.p.v);
  const placed: number[] = [];
  for (const l of labels) {
    let ly = y(l.p.v);
    for (const p of placed) if (Math.abs(ly - p) < 13) ly = p - 13;
    placed.push(ly);
  }

  const summary = series
    .map((s) => {
      const p = lastPoint(s);
      return `${s.label} ${p ? p.v : "no data"}`;
    })
    .join("; ");

  return (
    <figure className="chartbox" style={{ margin: 0 }}>
      <figcaption>
        <p className="charttitle">{title}</p>
        <div className="chartlegend" aria-hidden="true">
          {series.map((s) => (
            <span key={s.label}>
              <svg width="22" height="8" aria-hidden="true">
                <line x1="0" y1="4" x2="22" y2="4" stroke={s.colour} strokeWidth="2.5" strokeDasharray={s.dashArray} />
              </svg>
              {s.label}
            </span>
          ))}
        </div>
      </figcaption>

      <div className="chartscroll">
        <svg
          viewBox={`0 0 ${W} ${H}`}
          width="100%"
          style={{ minWidth: 560 }}
          role="img"
          aria-label={`${title}, in ${unit}, from 0 to ${playhead} seconds into the run. At the playhead: ${summary}. The full numbers are in the table below this chart.`}
        >
          {/* horizontal grid + y labels */}
          {Array.from({ length: yTicks + 1 }, (_, i) => {
            const v = (yMax / yTicks) * i;
            return (
              <g key={i}>
                <line x1={PAD.left} y1={y(v)} x2={PAD.left + iw} y2={y(v)} stroke="#d8e0e1" strokeWidth="1" />
                <text x={PAD.left - 8} y={y(v) + 3.5} textAnchor="end" fontFamily="var(--font-mono), monospace" fontSize="10" fill="#5d666a">
                  {v >= 100 ? Math.round(v) : Math.round(v * 10) / 10}
                </text>
              </g>
            );
          })}

          {/* the load event, bracketed from the k6 stage list */}
          {event.map((e, i) => (
            <line key={i} x1={x(e)} y1={PAD.top} x2={x(e)} y2={PAD.top + ih} stroke="#101619" strokeWidth="1" strokeDasharray="3 3" opacity="0.34" />
          ))}

          {/* x labels */}
          {Array.from({ length: xTicks + 1 }, (_, i) => {
            const t = (RUN_SECONDS / xTicks) * i;
            return (
              <text key={i} x={x(t)} y={H - 10} textAnchor="middle" fontFamily="var(--font-mono), monospace" fontSize="10" fill="#5d666a">
                {t}
              </text>
            );
          })}
          <text x={PAD.left + iw / 2} y={H - 0.5} textAnchor="middle" fontFamily="var(--font-sans), sans-serif" fontSize="10" fill="#5d666a">
            seconds into run
          </text>

          {/* the playhead itself */}
          <line x1={x(playhead)} y1={PAD.top} x2={x(playhead)} y2={PAD.top + ih} stroke="#8c2f39" strokeWidth="1" opacity="0.4" />

          {series.map((s) => (
            <path key={s.label} d={pathFor(s)} fill="none" stroke={s.colour} strokeWidth="2" strokeDasharray={s.dashArray} strokeLinejoin="round" strokeLinecap="round" />
          ))}

          {/* direct labels — never rely on colour alone */}
          {labels.map((l, i) => (
            <text key={l.s.label} x={PAD.left + iw + 6} y={placed[i] + 3.5} fontFamily="var(--font-sans), sans-serif" fontSize="10.5" fill={l.s.colour} fontWeight="600">
              {l.s.label}
            </text>
          ))}
        </svg>
      </div>

      <details className="datatable">
        <summary>Show the numbers behind this chart</summary>
        <div className="tablescroll">
          <table className="data">
            <caption className="visually-hidden">{title}, every sample up to the playhead, in {unit}</caption>
            <thead>
              <tr>
                <th scope="col">t (s)</th>
                {series.map((s) => (<th key={s.label} scope="col">{s.label}</th>))}
              </tr>
            </thead>
            <tbody>
              {series[0].points.filter((p) => p.t <= playhead).map((p, i) => (
                <tr key={p.t}>
                  <td>{p.t}</td>
                  {series.map((s) => (<td key={s.label}>{s.points[i]?.v ?? "—"}</td>))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </details>
    </figure>
  );
}
