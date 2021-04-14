%define	fontdir	%{_datadir}/fonts/Droidfont-tw

Summary: DroidFont for Taiwan
Name: droidfont-tw-fonts
Version: 2.55b
Release: 6.1
License: Apache License 2.0
Group: User Interface/X
BuildArch: noarch
Source0: https://github.com/pesder/Droidfont-tw/raw/master/DroidSansFallback.ttf
Source1: https://github.com/pesder/Droidfont-tw/raw/master/LICENSE.txt
URL: https://github.com/pesder/Droidfont-tw
Requires(post): fontconfig

%description
Based on DroidSansFallback Fonts with taiwan writting standard.

%prep
%setup -T -c

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{fontdir}
install -m644 %{SOURCE0} %{SOURCE1} %{buildroot}%{fontdir}

%clean
rm -rf %{buildroot}

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%{fontdir}/*

%changelog
* Sun Dec 06 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.55b
- Rebuilt for Fedora
