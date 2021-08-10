module.exports = {
  env: {
    es2021: true,
    browser: true,
  },
  extends: ['plugin:react/recommended', 'standard', 'prettier', 'plugin:prettier/recommended'],
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 12,
    sourceType: 'module',
  },
  plugins: ['react'],
  rules: {
    'react/prop-types': 0,
  },
};
