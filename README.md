<!-- Improved compatibility of back to top link: See: https://github.com/LoveDoLove/TpLinkFirmwareDirectory/pull/73 -->
<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]

<br />
<div align="center">
  <a href="https://github.com/LoveDoLove/TpLinkFirmwareDirectory">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">TpLinkFirmwareDirectory</h3>

  <p align="center">
    Python utility to list and export all firmware and app files from the public TP-Link S3 bucket.
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

TpLinkFirmwareDirectory is a Python utility that lists and exports all available firmware and app files from the public TP-Link S3 bucket (`download.tplinkcloud.com`). It is useful for researchers, developers, and users who want to audit, archive, or analyze TP-Link firmware and app releases.

The main script, `list_s3_files.py`, connects to the S3 bucket (with anonymous access), paginates through all objects, and writes the full list of keys to `all_keys.txt`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* Python 3.13+
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* [botocore](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.13 or newer
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```cmd
   git clone https://github.com/LoveDoLove/TpLinkFirmwareDirectory.git
   cd TpLinkFirmwareDirectory
   ```
2. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```
   Or, if using Poetry:
   ```cmd
   pip install poetry
   poetry install
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

To list all files in the TP-Link public S3 bucket and export them to `all_keys.txt`:

```cmd
python list_s3_files.py
```

- The output file `all_keys.txt` will contain one key per line, representing each file in the bucket.
- You can use this file for further analysis, archiving, or automation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [x] List all files in TP-Link public S3 bucket
- [ ] Add filtering by file type or prefix
- [ ] Export metadata (size, last modified, etc.)
- [ ] Add CLI options for custom buckets
- [ ] Add tests and CI

See the [open issues](https://github.com/LoveDoLove/TpLinkFirmwareDirectory/issues) for a full list of proposed features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

For bug reports and feature requests, use the provided GitHub issue templates.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/LoveDoLove/TpLinkFirmwareDirectory/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=LoveDoLove/TpLinkFirmwareDirectory" alt="contrib.rocks image" />
</a>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

LoveDoLove - [GitHub](https://github.com/LoveDoLove)

Project Link: [https://github.com/LoveDoLove/TpLinkFirmwareDirectory](https://github.com/LoveDoLove/TpLinkFirmwareDirectory)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* [botocore](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
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
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/
[product-screenshot]: images/logo.png
