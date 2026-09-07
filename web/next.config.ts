import type { NextConfig } from "next";

/**
 * Fully static. The site reads only committed JSON — no API routes, no server
 * rendering, no data fetching at request time — so there is nothing for a
 * server to do. `output: 'export'` emits plain files into out/, which is what
 * Vercel serves from its CDN.
 */
const nextConfig: NextConfig = {
  output: "export",
  images: { unoptimized: true },   // no server, so no on-demand image optimiser
  reactStrictMode: true,
};

export default nextConfig;
