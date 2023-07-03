%define	fontdir	%{_datadir}/fonts/wang

Summary: H.T.Wang Free Phonetic Fonts
Name: wang-phonetic-fonts
Version: 1.3.0
Release: 2.1
License: GPLv2
Group: User Interface/X
BuildArch: noarch
#Source0: https://wangfonts.googlecode.com/files/wangfonts-%{version}.tar.gz
Source0: %{name}-%{version}.txz
URL: https://code.google.com/p/wangfonts/
Requires(post): fontconfig
Requires: wang-fonts

%description
Free Chinese TrueType phonetic fonts 2004 donated by Prof. Hann-Tzong WANG.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{fontdir}
install -m644 wp*.ttf %{buildroot}%{fontdir}

%clean
rm -rf %{buildroot}

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%{fontdir}/wp*.ttf

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.0
- Rebuilt for Fedora
