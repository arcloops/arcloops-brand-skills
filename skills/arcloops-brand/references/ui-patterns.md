# UI, web and mobile patterns

Goal: designs that feel engineered and calm, with unmistakable color. Never a gray wireframe.

## Components
- **Primary button, light surface**: charcoal fill, white Geist SemiBold label. **Highlight CTA**: magenta fill, white label at 18px+ semibold. **On dark**: cyan fill with charcoal label.
- **Secondary button**: 1px charcoal outline (white outline on dark), no fill.
- **Link**: charcoal underlined on light, cyan on dark.
- **Input**: white, 1px #D9D9D9 border, 4px radius; focus = 2px magenta ring (cyan on dark).
- **Chips and badges**: tint background + charcoal text + small solid dot in the brand color (info cyan, warning amber, error magenta). Add an icon and a word.
- **Card**: white, 1px hairline, square or 4px radius, no shadow. Optional 3px top rule in a brand color (rotate cyan / magenta / amber across a row).
- **Tabs**: charcoal text, active tab gets a 3px cyan (light) or magenta underline.
- **Table**: hairline rows, #F7F7F7 header, numerals right-aligned in Geist.
- **Nav (web)**: white bar with hairline, or charcoal sidebar with cyan active marker.
- **Charts**: series order cyan, magenta, amber, charcoal, gray. Label directly, differentiate lines by dash style or markers as well as color. Axes and grid in #D9D9D9 / gray.
- **Empty states**: concentric-arc line art in gray with one brand-colored arc, a one-line outcome message, one button.

## Web page recipes
1. **Charcoal hero**: charcoal ground, Geist Bold white headline (56 to 96px), cyan CTA, large full-color loop cropped at the right edge, gradient 4px rule under the hero.
2. **ARC triad**: three equal panels, cyan with charcoal letter and text, magenta with white, amber with charcoal. Giant A / R / C in Geist Bold.
3. **Process strip**: Audit, Consult, Train, Build as four columns, gray numerals, a 3px top rule per column cycling the brand colors.
4. **Stat band**: #F7F7F7 band, four big Geist numerals (one colored by a brand color at 48px+), caption underneath.
5. **Color-blocked CTA band**: full-width magenta (white text 28px+) or cyan/amber (charcoal text), single charcoal button.
6. **Quote or proof**: white, hairlines, large numerals, no stock photos; logos in gray.
7. **Footer**: charcoal, `-03` logo, links in white, hairline dividers, cyan hover.
8. **Gradient hairline** as section separator or under the header (2 to 4px).

## Dashboard recipes
- Charcoal sidebar (logo `-03`), white workspace, #F7F7F7 page ground optional.
- KPI tiles in a row, each with a 3px top rule in a different brand color, Geist numeral 32 to 40px, delta with arrow icon and label.
- One primary chart (cyan lead series), secondary charts using the series order above.
- Status chips in tables; toast and alert bars use tint backgrounds with a 4px left rule in the status color.
- Dark mode: charcoal #38393B ground, hairlines in rgba(255,255,255,.14), text in white, cyan and amber. No extra dark grays.

## Mobile (iOS and Android) recipes
- Canvas 390 x 844. Respect safe areas. Touch targets 44px minimum. Body 16, caption 12 minimum.
- **Splash / welcome**: charcoal, full-color loop centered or bleeding off the corner, logo `-03` or `-02`, one cyan button.
- **Home**: white, Geist greeting, one hero card with gradient hairline, list of rows with hairlines, bottom tab bar (5 max) with active item in charcoal plus a 3px cyan bar.
- **Detail / status**: large Geist title, status chip, key facts table, sticky bottom CTA (charcoal or magenta).
- **Onboarding**: three screens, each with one brand color as the lead (cyan, magenta, amber panel with charcoal or white Geist headline), progress dots in charcoal.
- **Notifications / toasts**: tint background, left status rule, icon plus text.
- App icon: no icon vector exists. Use the full-color loop cropped on charcoal only after the owner approves.

## More ideas
- Report cover: charcoal with cropped gradient loop, white Geist title. Inside pages: white, colored numerals for section numbers.
- Social post: color-blocked square (cyan / magenta / amber) with a large charcoal or white statement, logo `-03` or `-04` bottom-left, loop crop bleeding off one corner.
- LinkedIn banner 1584 x 396: charcoal, loop at the right, headline white, thin gradient rule.
- Email: white, charcoal text, one cyan or magenta button, gradient hairline under the logo.
- Slide dividers: full magenta or cyan slide with a giant numeral in Geist Bold.
- Loading: concentric arc line animation is NOT specified; keep it static or a simple fade until motion rules exist.

## Don't
- Don't use cyan or amber as small text on white. Don't put white text on cyan or amber.
- Don't mix more than one lead accent as large fields on a screen.
- Don't use shadows, glassmorphism, neon glows, or stock gradients. Gradient is cyan → magenta → amber only.
- Don't draw your own icon mark or distort the rings.
