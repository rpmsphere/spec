Name: firefox-extensions
Version: 2012
Release: 1
Summary: Firefox Extensions (NewTongwen, PDFdownload, YouTubeDownloader)
License: GPL
Group: Networking/WWW
Source0: http://www.openfoundry.org/of/download_path/tongwen/0.4/tongwen_0.4.0.7.1.xpi
Source1: https://addons.mozilla.org/firefox/downloads/latest/636/addon-636-latest.xpi
Source2: http://www.heapr.com/chrome/youtube_downloader_firefox.xpi
BuildArch: noarch
Requires: firefox

%description
NewTongwen: Switching Between Simplified- and Traditional-Chinese
PDFdownload: Downloader for PDF files
YouTubeDownloader: Download any YouTube video file

%prep
%setup -T -c

%build

%install
%__rm -rf %{buildroot}
%__install -D -m 644 %{SOURCE0} %{buildroot}/usr/lib/firefox-extensions/tongwen_0.4.0.7.1.xpi
%__install -D -m 644 %{SOURCE1} %{buildroot}/usr/lib/firefox-extensions/addon-636-latest.xpi
%__install -D -m 644 %{SOURCE2} %{buildroot}/usr/lib/firefox-extensions/youtube_downloader_firefox.xpi

%clean
%__rm -rf %{buildroot}

%post 
firefox -install-global-extension /usr/lib/firefox-extensions/tongwen_0.4.0.7.1.xpi
firefox -install-global-extension /usr/lib/firefox-extensions/addon-636-latest.xpi
firefox -install-global-extension /usr/lib/firefox-extensions/youtube_downloader_firefox.xpi

%files
%defattr(-,root,root)
/usr/lib/firefox-extensions

%changelog
* Tue Mar 06 2012 Wei-Lun Chao <bluebat@member.fsf.org> 2012-1
- Add more extensions

* Wed Oct 03 2007 Wei-Lun Chao <bluebat@member.fsf.org> 20071003-1
- Initial package
