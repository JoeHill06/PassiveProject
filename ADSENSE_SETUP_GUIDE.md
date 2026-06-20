# Google AdSense Setup Guide for GradeCalc

## Current AdSense Review Status

As of 20 June 2026, the local and live site checks show:

- `https://gradecalc.online/ads.txt` returns `200` and contains the correct publisher line:
  `google.com, pub-1852446478186734, DIRECT, f08c47fec0942fa0`
- The screenshot status "Not found" is most likely stale from AdSense's last crawl. In AdSense, open **Sites** -> `gradecalc.online` -> **Check for updates** after deploying.
- The remaining rejection issue is "Low value content". The site now publishes a clearer homepage methodology section, an editorial policy, labelled ad placements, updated sitemap metadata, and no longer serves the thin legacy redirect page.

Before requesting review again:

1. Deploy the regenerated `docs/` folder.
2. Confirm `https://gradecalc.online/ads.txt` still displays the publisher line above.
3. In AdSense, use **Check for updates** on the ads.txt status.
4. Request another site review after AdSense shows the ads.txt file as found or authorized.

## Step 1: Apply for Google AdSense

### Requirements:
- ✅ Custom domain (gradecalc.online)
- ✅ HTTPS enabled
- ✅ Quality content and original tools
- ✅ Privacy Policy page
- ✅ Root `ads.txt` file published
- ⏳ Some traffic (recommended but not always required)

### How to Apply:
1. Go to: https://www.google.com/adsense
2. Click "Get Started"
3. Enter your URL: `https://gradecalc.online`
4. Fill in your payment details
5. Submit application
6. Wait 1-4 weeks for approval

---

## Step 2: Add AdSense Code to Your Site

### Once Approved:

**Option A: Auto Ads (Easiest)**

1. In your AdSense dashboard, go to **Ads** → **Overview**
2. Copy your AdSense code (looks like this):
```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX"
     crossorigin="anonymous"></script>
```

3. Open `templates/base.html`
4. Find the commented AdSense section (around line 18-22)
5. **Uncomment** the code and replace `ca-pub-XXXXXXXXXXXXXXXX` with your actual publisher ID
6. Save, commit, and push to GitHub

**Before (commented out):**
```html
<!--
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX"
     crossorigin="anonymous"></script>
-->
```

**After (uncommented with your ID):**
```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1234567890123456"
     crossorigin="anonymous"></script>
```

**Option B: Manual Ad Placement (More Control)**

Create ad units in AdSense and place them manually:

### Recommended Ad Placements:

**1. Above Calculator (Display Ad)**
Place in calculator HTML files before the calculator starts:
```html
<!-- Ad: Above Calculator -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
     data-ad-slot="1234567890"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
```

**2. Below Calculator (Display Ad)**
Place after results section

**3. Sidebar Ad (if you add a sidebar)**

**4. In-Article Ads (in guides)**
Place between paragraphs in guide pages

---

## Step 3: Git Commands to Deploy

```bash
# After editing base.html with your AdSense code:
git add templates/base.html
git commit -m "Add Google AdSense code for monetization"
git push origin main
```

Wait 2 minutes for GitHub Actions to deploy.

---

## Payment Information

### How Much Can You Earn?

**Revenue Per 1,000 Visitors (RPM):**
- Education niche: $2 - $10 RPM
- With 1,000 visitors/month = $2-10/month
- With 10,000 visitors/month = $20-100/month
- With 100,000 visitors/month = $200-1,000/month

**Factors Affecting Earnings:**
- Visitor location (US/UK = higher CPM)
- Ad placement
- User engagement
- Season (higher during exam periods)

### Payment Details:
- **Minimum payout:** $100
- **Payment method:** Bank transfer, check, or wire
- **Payment schedule:** Monthly (around 21st of each month)
- **Tax info:** You'll need to fill out tax forms

### Example Calculation:
- 5,000 visitors/month
- 50% ad viewability rate = 2,500 ad impressions
- $5 CPM (cost per 1,000 impressions)
- **Earnings:** $12.50/month

You need consistent traffic to reach the $100 minimum payout.

---

## Tips to Maximize Ad Revenue

### 1. Strategic Ad Placement:
- ✅ Above the fold (visible without scrolling)
- ✅ After calculator results
- ✅ Between guide sections
- ❌ Don't overload with ads (hurts user experience)

### 2. Increase Traffic:
- SEO optimization (you've done this)
- Share on student forums (Reddit, TheStudentRoom)
- Create more calculators
- Update content regularly

### 3. Ad Optimization:
- Use responsive ad units
- Enable Auto Ads to find best placements
- A/B test different ad positions
- Monitor AdSense reports

### 4. Comply with AdSense Policies:
- ✅ Don't click your own ads
- ✅ Don't ask users to click ads
- ✅ Don't place ads on error pages
- ✅ Ensure ads are clearly labeled

---

## Alternative Ad Networks

If AdSense rejects you or you want additional revenue:

### 1. **Media.net** (contextual ads)
- Good alternative to AdSense
- Works with Yahoo/Bing
- Apply: https://www.media.net

### 2. **Ezoic** (AI-driven ads)
- Requires 10,000 monthly visitors
- Higher RPM than AdSense
- Apply: https://www.ezoic.com

### 3. **PropellerAds** (easier approval)
- Lower quality ads
- Lower earnings
- Apply: https://propellerads.com

### 4. **Affiliate Marketing** (alternative monetization)
- Amazon Associates
- Course platforms (Udemy, Coursera)
- Student tool affiliates
- Can earn more per conversion

---

## Monitoring Your Earnings

### AdSense Dashboard:
- **Reports** - See daily earnings
- **Performance by page** - Which calculators earn most
- **Optimization ideas** - Google's suggestions

### Key Metrics to Track:
- **Page RPM** - Revenue per 1,000 pageviews
- **Impressions** - How many ads shown
- **CTR** - Click-through rate
- **CPC** - Cost per click

---

## Troubleshooting

### "Site Not Approved"
- **Reason:** Insufficient content or traffic
- **Solution:** Wait 2-3 months, build traffic, reapply

### "Ads Not Showing"
- Check AdSense code is uncommented
- Wait 24 hours after adding code
- Check browser ad blockers are disabled
- Verify site is approved in AdSense dashboard

### "Low Earnings"
- **Solution:** Increase traffic (SEO, marketing)
- Optimize ad placements
- Target high-value keywords

---

## Quick Checklist

Before applying:
- [ ] HTTPS enabled (SSL certificate issued)
- [ ] Privacy policy page published
- [ ] Site has quality content
- [ ] Domain is verified in Google Search Console
- [ ] Some traffic (500+ visitors/month recommended)

After approval:
- [ ] Add AdSense code to `base.html`
- [ ] Uncomment the script
- [ ] Replace `ca-pub-XXXXX` with your ID
- [ ] Commit and push to GitHub
- [ ] Wait 24 hours for ads to appear
- [ ] Monitor earnings in AdSense dashboard

---

## Current Status: Ready to Re-submit After Deploy

**Next steps:**
1. Deploy the current `docs/` build to GitHub Pages
2. Click **Check for updates** for `ads.txt` in AdSense
3. Request review for `gradecalc.online`
4. While waiting, keep publishing useful calculators/guides and building organic traffic

**Expected Timeline:**
- AdSense ads.txt refresh: a few days, sometimes longer on low-traffic sites
- AdSense site review: 1-4 weeks
- First $100 payout: 2-6 months (depending on traffic)
