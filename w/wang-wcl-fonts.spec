%define	fontdir	%{_datadir}/fonts/wang

Summary: H.T.Wang WCL Fonts
Name: wang-wcl-fonts
Version: 1.0
Release: 2.1
License: GPLv2
Group: User Interface/X
BuildArch: noarch
Source0: font_wong.zip
URL: https://code.google.com/p/wangfonts/
Requires(post): fontconfig

%description
Free Chinese TrueType fonts 2000 donated by Prof. Hann-Tzong WANG.

%prep
%setup -q -n font_wong

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{fontdir}
install -m644 *.ttf %{buildroot}%{fontdir}

%clean
rm -rf %{buildroot}

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%{fontdir}/*

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
