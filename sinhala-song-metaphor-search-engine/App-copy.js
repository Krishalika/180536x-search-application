import React from "react";

import ElasticsearchAPIConnector from "@elastic/search-ui-elasticsearch-connector";

import {
  ErrorBoundary,
  Facet,
  SearchProvider,
  SearchBox,
  Results,
  PagingInfo,
  ResultsPerPage,
  Paging,
  WithSearch
} from "@elastic/react-search-ui";
import { Layout } from "@elastic/react-search-ui-views";
import "@elastic/react-search-ui-views/lib/styles/styles.css";

const connector = new ElasticsearchAPIConnector({
  cloud: {
    id: "search-engine:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyRlMzljMzkwMTRmZTQ0YmUzYjNhNGY3M2VkZGMyZjcwYiQwZjIyNzJlZTFlZGM0NGRjOTM5NjFhM2IwYTc3ZjQ1Zg=="
  },
  apiKey: "VlVqN3U0VUJnNjZCUU14ejZQeDg6YVhzblctZUZUd3EtM2NpcF8xdVJUUQ==",
  index: "search-engine"
});

const config = {
  searchQuery: {
    search_fields: {
      Target: {
        weight: 3
      },
    },
    sort: {
      "Title.keyword": { order: "asc" } 
      },
    result_fields: {
      Title: {
        snippet: {},
        keyword: {}
      },
      Singer: {
        snippet: {}
      },
      Composer: {
        snippet: {}
      },
      Lyricist: {
        snippet: {}
      },
      Album: {
        snippet: {}
      },
      Year: {
        snippet: {}
      },
      Lyrics: {
        snippet: {}
      },
      Metaphor: {
        snippet: {}
      },
      Source: {
        snippet: {}
      },
      Target: {
        snippet: {}
      },
      Interpretation: {
        snippet: {}
      },
      Genre: {
        snippet: {}
      }
    },
    disjunctiveFacets: ["Singer.keyword", "Composer.keyword", "Lyricist.keyword"],
    facets: {
      "Singer.keyword": { type: "value" },
      "Composer.keyword": { type: "value" },
      "Lyricist.keyword": { type: "value" },     
    }
  },

  autocompleteQuery: {
    results: {
      resultsPerPage: 5,
      search_fields: {
        "Target.suggest": {
          weight: 3
        }
      },
      result_fields: {
        Target: {
          snippet: {
            size: 100,
            fallback: true
          }
        },
      }
    },
    suggestions: {
      types: {
        results: { fields: ["Target"] }
      },
      size: 4
    }
  },

  apiConnector: connector,
  alwaysSearchOnInitialLoad: true
};

export default function App() {
  return (
    <SearchProvider config={config}>
      <WithSearch mapContextToProps={({ wasSearched }) => ({ wasSearched })}>
        {({ wasSearched }) => {
          return (
            <div className="App">
              <ErrorBoundary>
                <Layout
                  header={<SearchBox autocompleteSuggestions={false} />}
                  sideContent={
                    <div>
                      <Facet key={"1"} field={"Singer.keyword"} label={"Singer"} />
                      <Facet key={"2"} field={"Composer.keyword"} label={"Composer"} />
                      <Facet key={"3"} field={"Lyricist.keyword"} label={"Lyricist"} />
                    </div>
                  }
                  bodyContent={
                    <Results shouldTrackClickThrough={true} />
                  }
                  bodyHeader={
                    <React.Fragment>
                      {wasSearched && <PagingInfo />}
                      {wasSearched && <ResultsPerPage />}
                    </React.Fragment>
                  }
                  bodyFooter={<Paging />}
                />
              </ErrorBoundary>
            </div>
          );
        }}
      </WithSearch>
    </SearchProvider>
  );
}