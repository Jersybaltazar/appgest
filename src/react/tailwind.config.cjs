/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./web/purchase_order_sheet/**/*.{js,ts,jsx,tsx}",
    "./web/product_rpc/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        invoice: ["Inconsolata", "mono"],
      },
    },
  },
  plugins: [],
}
