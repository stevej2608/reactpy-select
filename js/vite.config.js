import { defineConfig } from 'vite'
import {resolve } from "path";
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig(({ command, mode }) => {
  console.log('command=[%s], mode=[%s]', command, mode)

  const isDev = ['dev', 'development'].includes(mode)

  return {
    plugins: [react()],

    define: {
      'process.env': process.env
    },

    build: {
      sourcemap: isDev ? false : false,
      minify: 'terser',
      // minify: isDev ? false : true,

      outDir: "../reactpy_select",
      emptyOutDir : false,

      // https://vitejs.dev/guide/build.html#library-mode
      
      lib: {
        // Could also be a dictionary or array of multiple entry points
        entry: resolve(__dirname, './src/index.js'),
        name: 'reactpy-select',
        // the proper extensions will be added
        fileName: isDev ? 'bundle.dev' : 'bundle.min',
        formats: ['es']
      },
      rollupOptions: {
        // external: ['react', 'react-dom'],
      },
    },
  }

})
