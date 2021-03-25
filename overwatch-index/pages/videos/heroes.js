// import fs from "fs";
// import path from "path";
import Link from "next/link";

import { getSortedVideosData } from "../../lib/videos";

export async function getStaticProps() {
  const allVideosData = getSortedVideosData();
  return {
    props: {
      allVideosData,
    },
  };
}

export default function HeroList({ allVideosData }) {
  return (
    <>
      <h1>Heroes</h1>
      <h2>
        <Link href="/">
          <ul>
            {Object.entries(allVideosData["heroes"]).map(([hero, data]) => {
              if (data.videos === undefined) return;
              return (
                <li key={hero}>
                  {hero} - {data.videos.length}
                </li>
              );
            })}
          </ul>
        </Link>
      </h2>
    </>
  );
}
