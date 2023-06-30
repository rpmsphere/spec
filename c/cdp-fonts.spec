%define fontname cdp
%define	fontdir	%{_datadir}/fonts/%{fontname}

Summary: Fonts from Chinese Documents Processing Lab
Name: %{fontname}-fonts
Version: 2.65
Release: 1
License: GFDL1.2 or CC-BY-SA 2.5 TW
Group: User Interface/X
BuildArch: noarch
Source: cdpfonts265.zip
URL: https://cdp.sinica.edu.tw/
Requires(post): fontconfig

%description
Ancient chinese fonts from Chinese Documents Processing Lab.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{fontdir}
install -m 0644 *.ttf $RPM_BUILD_ROOT%{fontdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%{fontdir}

%changelog
* Tue Nov 26 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.65
- Rebuilt for Fedora
