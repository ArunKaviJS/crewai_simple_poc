from schemas.article import ArticleDraft
from schemas.social import SocialDrafts


def publish_gate(
    article: ArticleDraft,
    social: SocialDrafts
) -> bool:

    print("\n")
    print("=" * 70)
    print("                    PUBLISH GATE")
    print("=" * 70)

    print("\nARTICLE")
    print("-" * 70)

    print(f"\nTITLE:\n{article.title}")

    print(f"\nSUMMARY:\n{article.summary}")

    print(
        f"\nARTICLE:\n"
        f"{article.article_markdown}"
    )

    print("\nLINKEDIN")
    print("-" * 70)
    print(social.linkedin_post)

    print("\nX")
    print("-" * 70)
    print(social.x_post)

    print("\n" + "=" * 70)

    answer = input(
        "\nApprove for publishing? "
        "[y/N]: "
    ).strip().lower()

    return answer in {"y", "yes"}