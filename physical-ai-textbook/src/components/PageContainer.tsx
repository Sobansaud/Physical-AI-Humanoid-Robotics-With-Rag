import React from 'react';

type Props = {children: React.ReactNode};

export default function PageContainer({children}: Props): JSX.Element {
  return (
    <div style={{padding: '2rem 0'}}>
      <main className="theme-doc-markdown card-glassmorphism">{children}</main>
    </div>
  );
}
