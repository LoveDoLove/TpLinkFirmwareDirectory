<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

<br />
<div align="center">
  <a href="https://github.com/LoveDoLove/TpLinkFirmwareDirectory">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">TP-Link Firmware Directory</h3>

  <p align="center">
    A Python utility to fetch and list all firmware and application files from the TP-Link cloud S3 bucket, exporting the results to a text file for research or archival purposes.
    <br />
    <a href="https://github.com/LoveDoLove/TpLinkFirmwareDirectory"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/LoveDoLove/TpLinkFirmwareDirectory">View Demo</a>
    &middot;
    <a href="https://github.com/LoveDoLove/TpLinkFirmwareDirectory/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/LoveDoLove/TpLinkFirmwareDirectory/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

This project provides a Python script to enumerate and export all file keys from the TP-Link firmware and application S3 bucket (`download.tplinkcloud.com`). The output is a comprehensive list of available files, including firmware, apps, and configuration files, useful for research, analysis, or archival.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- Python 3.13+
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [botocore](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- Python 3.13 or higher
- pip (Python package manager)

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/LoveDoLove/TpLinkFirmwareDirectory.git
   ```
2. Change into the project directory
   ```sh
   cd TpLinkFirmwareDirectory
   ```
3. (Optional but recommended) Create and activate a virtual environment
   ```sh
   python -m venv .venv
   .venv\Scripts\activate
   ```
4. Install dependencies
   ```sh
   pip install -r requirements.txt
   # or, if using pyproject.toml/PEP 621:
   pip install .
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

Run the main script to fetch and export all S3 object keys from the TP-Link cloud bucket:

```sh
python .github/scripts/fetch_s3_firmware_list.py
```

The output will be saved to `lists/download.tplinkcloud.com_all_keys.txt`.

You can then analyze or process this file as needed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

See the [open issues](https://github.com/LoveDoLove/TpLinkFirmwareDirectory/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/LoveDoLove/TpLinkFirmwareDirectory/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=LoveDoLove/TpLinkFirmwareDirectory" alt="contrib.rocks image" />
</a>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

LoveDoLove

Project Link: [https://github.com/LoveDoLove/TpLinkFirmwareDirectory](https://github.com/LoveDoLove/TpLinkFirmwareDirectory)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [botocore](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/LoveDoLove/TpLinkFirmwareDirectory.svg?style=for-the-badge
[contributors-url]: https://github.com/LoveDoLove/TpLinkFirmwareDirectory/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/LoveDoLove/TpLinkFirmwareDirectory.svg?style=for-the-badge
[forks-url]: https://github.com/LoveDoLove/TpLinkFirmwareDirectory/network/members
[stars-shield]: https://img.shields.io/github/stars/LoveDoLove/TpLinkFirmwareDirectory.svg?style=for-the-badge
[stars-url]: https://github.com/LoveDoLove/TpLinkFirmwareDirectory/stargazers
[issues-shield]: https://img.shields.io/github/issues/LoveDoLove/TpLinkFirmwareDirectory.svg?style=for-the-badge
[issues-url]: https://github.com/LoveDoLove/TpLinkFirmwareDirectory/issues
[license-shield]: https://img.shields.io/github/license/LoveDoLove/TpLinkFirmwareDirectory.svg?style=for-the-badge
[license-url]: https://github.com/LoveDoLove/TpLinkFirmwareDirectory/blob/main/LICENSE
