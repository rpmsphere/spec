%define	fontdir	%{_datadir}/fonts/hdzb

Summary: Free chinese HDZB Fonts
Name: hdzb-fonts
Version: 1.2
Release: 2.1
License: Unknown
Group: User Interface/X
BuildArch: noarch
Source0: HDZB-fonts.zip
URL: https://www.freegroup.org/2009/09/free-chinese-fonts-hdzb/
Requires(post): fontconfig

%description
A small but nice collection of fonts from the HDZB collection.
(C) 1994-1997, BeiJing HanDing Inc.

%prep
%setup -q -c

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
%{fontdir}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
