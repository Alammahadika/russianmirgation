# Russian Migration Policy Discoure Central Asia News
This project is my thesis on Russian Migration Policy Issues within the framework of Central Asian News discourse. My thesis has collected data, analyzed data, and visualized data mostly using machine learning.
Indicator research for analysis im used Issue Migration Policy according [Julia Mendelsohn, Ceren Budak, David Jurgens in Modeling Framing in Immigration Discourse on Social Media](https://aclanthology.org/2021.naacl-main.179.pdf)

| Frame                | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **Economy**          | Financial problems; remittances, low wages, economic growth                 |
| **Capacity and Resources** | Physical resources and human resources availability                      |
| **Morality and Ethic** | Perspective driven by religion or sense of ethics                         |
| **Justice and Equality** | Inequality in the redistribution of law and punishment                    |
| **Crime and Punishment** | Court cases, consequences of breaking the law and implications of threats |
| **Safety**           | Safety considerations of a policy issue                                    |
| **Quality Life**     | Impact on life and life routines                                           |
| **Culture Identity** | Assimilation/Integration efforts and customs                               |
| **Public Sentiment** | Social norms, sentiments of prejudice, good and bad                        |
| **Political Implication** | Policy decisions, migrant involvement in migration policy               |
| **External Regulator** | Agreements and intergovernmental relations                                |

From the table above, analysis can be carried out to determine the indicators and variables in the analysis results.

### State of Arts
In the literature review, this thesis uses keywords based on 1,258 studies on Discourse Migration Policy. All studies were collected from the Scopus Site and created Events and keywords in VOSViewers, then the data was cleaned and produced 32 main keywords.

## 📊 Migration-Related Keywords Frequency Analysis

| Keyword                | Occurrences | Visual Representation       |
|------------------------|-------------|-----------------------------|
| **Migration**          | 472         | ████████████████████████     |
| **Immigration Policy** | 238         | █████████████                |
| **International Migration** | 147    | █████████                    |
| **Refugee**            | 103         | ██████                       |
| **Immigration**        | 115         | ██████                       |
| **Immigrant**          | 67          | ████                         |
| **Refugees**           | 64          | ████                         |
| **Political Discourse** | 58       | ███                          |
| **Immigrant Population** | 55       | ███                          |
| **Asylum Seeker**      | 52          | ███                          |
| **Human Rights**       | 57          | ███                          |
| **Forced Migration**   | 53          | ███                          |
| **Multiculturalism**   | 51          | ███                          |

<details>
<summary>📈 Show More Keywords (20+)</summary>

| Keyword                | Occurrences | Visual Representation       |
|------------------------|-------------|-----------------------------|
| **Labor Migration**    | 46          | ██                          |
| **Population Migration** | 45       | ██                          |
| **Racism**             | 41          | ██                          |
| **Migration Policy**   | 48          | ██                          |
| **Migration Experience** | 28       | █                           |
| **Borders**            | 23          | █                           |
| **Migration Determinant** | 21     | █                           |
| **Refugee Crisis**     | 24          | █                           |
| **Trafficking**        | 20          | █                           |
| **Violence**           | 16          | █                           |
| **Discrimination**     | 13          | █                           |
| **Xenophobia**         | 12          | █                           |
| **Illegal Immigrant**  | 11          | █                           |
| **Migration Crisis**   | 10          | █                           |
| **Mass Media**         | 9           | █                           |
| **Migrants Remittance** | 7        | █                           |
| **Health Worker**      | 6           | █                           |
| **Media Discourse**    | 5           | █                           |
| **Islamophobia**       | 4           | █                           |
</details>


### 📊 Keywords in Migration Policy Research

```r
library(ggplot2)
library(ggrepel)

# Create visually enhanced scatter plot of keyword frequencies
ggplot(keywordsmigrationpolicy, aes(x = Selected, y = Occurences)) +
  geom_point(aes(color = ifelse(Keyword %in% c("Media Discourse", "Mass Media"), "red", "black")),
             size = 0, alpha = 0.7) +
  
  # Smart labeling to avoid overlap
  geom_text_repel(aes(label = Keyword, 
                  color = ifelse(Keyword %in% c("Media Discourse", "Mass Media"), 
                                "red", "black")),
                  size = 3.5,
                  max.overlaps = 30,
                  box.padding = 0.5,
                  segment.color = 'grey50') +
  
  # Trend line
  geom_smooth(method = "loess", se = FALSE, color = "blue", linetype = "dashed") +
  
  # Labels and titles
  labs(title = "Keyword Frequency in Migration Policy Research",
       subtitle = "Analysis of Academic Literature (n = 1,500+ articles)",
       x = "Keyword Categories",
       y = "Frequency Count",
       caption = "Note: Media-related keywords highlighted in red") +
  
  # Visual enhancements
  ylim(min(keywordsmigrationpolicy$Occurences) - 10,
       max(keywordsmigrationpolicy$Occurences) + 10) +
  scale_color_identity() +
  theme_minimal() +
  theme(
    plot.title = element_text(face = "bold", size = 14, hjust = 0.5),
    plot.subtitle = element_text(hjust = 0.5, color = "gray40"),
    panel.grid.major = element_line(color = "gray90"),
    axis.title = element_text(face = "bold")
  )
```


![Keyword Frequency in Migration](datavisual/16c5308f-0603-47ce-849e-d16b9e1ade8c.png)
