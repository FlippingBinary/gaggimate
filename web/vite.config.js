import { defineConfig } from 'vite';
import preact from '@preact/preset-vite';

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    outDir: '../data',
    emptyOutDir: true,
  },

  plugins: [preact()],

  server: {
    proxy: {
      '/api': {
        target: 'http://gaggimate.local/',
        changeOrigin: true,
      },
      '/ws': {
        target: 'ws://gaggimate.local',
        ws: true,
      }
    },
  },
});
