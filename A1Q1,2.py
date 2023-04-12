{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMZh095ngK4auk+MQFyIp2q",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/zeeshankhan00/Data-Science/blob/main/A1Q1%2C2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S5kNVjIqvHvm",
        "outputId": "74406e92-3b29-4521-ccbb-9ee53a02c19d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{8.7: 83000.0, 8.1: 88000.0, 0.7: 48000.0, 6: 76000.0, 6.5: 69000.0, 2.5: 60000.0, 10: 83000.0, 1.9: 48000.0, 4.2: 63000.0}\n",
            "defaultdict(<class 'list'>, {'more than five': [83000, 88000, 76000, 69000, 76000, 83000], 'less than two': [48000, 48000], 'between two and five': [60000, 63000]})\n",
            "{8.7: 'paid', 8.1: 'paid', 0.7: 'unpaid', 6: 'paid', 6.5: 'paid', 2.5: 'paid', 10: 'paid', 1.9: 'unpaid', 4.2: 'paid'}\n"
          ]
        }
      ],
      "source": [
        "from collections import defaultdict\n",
        "salaries_by_tenure = [(83000,8.7),(88000,8.1),\n",
        "                      (48000,0.7),(76000,6),\n",
        "                      (69000,6.5),(76000,6),\n",
        "                      (60000,2.5),(83000,10),\n",
        "                      (48000,1.9),(63000,4.2)]\n",
        "salary_by_tenure = defaultdict(list)\n",
        "for salary,tenure in salaries_by_tenure:\n",
        "  salary_by_tenure[tenure].append(salary)\n",
        "\n",
        "average_salary_by_tenure = {\n",
        "    tenure:sum(salaries)/len(salaries)\n",
        "    for tenure,salaries in salary_by_tenure.items()\n",
        "}\n",
        "\n",
        "print(average_salary_by_tenure)\n",
        "\n",
        "def tenure_bucket(tenure):\n",
        "  if tenure<2:\n",
        "    return \"less than two\"\n",
        "  elif tenure<5:\n",
        "    return \"between two and five\"\n",
        "  else:\n",
        "    return \"more than five\"\n",
        "salary_by_tenure2 = defaultdict(list)\n",
        "for salary, tenure in salaries_by_tenure:\n",
        "  bucket = tenure_bucket(tenure)\n",
        "  salary_by_tenure2[bucket].append(salary)\n",
        "print(salary_by_tenure2)\n",
        "\n",
        "def predict_paid_or_unpaid(years_experience):\n",
        "  if years_experience<2.0:\n",
        "    return \"unpaid\"\n",
        "  else:\n",
        "    return \"paid\"\n",
        "\n",
        "paid_or_unpaid3 = {\n",
        "    tenure:predict_paid_or_unpaid(tenure)\n",
        "    for tenure,salaries in salary_by_tenure.items()\n",
        "}\n",
        "\n",
        "print(paid_or_unpaid3)"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "iqBG7TBj6VPz"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}