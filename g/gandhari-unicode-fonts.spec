%define	fontdir	%{_datadir}/fonts/gandhari-unicode

Name:           gandhari-unicode-fonts
Version:        5.110
Release:        3.1
Summary:        A romanization font for writing Gāndhārī in transliteration as well as many other languages
License:        GPL
Group:          System/X11/Fonts
URL:            http://ebmp.org/p_dwnlds.php
Source:         http://andrewglass.org/downloads/gu5-110_ttf.zip
BuildArch:      noarch

%description
The Gandhari Unicode font is a modification of the Nimbus Roman No9 font.
It has been modified by Andrew Glass (asg@alumni.washington.edu) for
the Early Buddhist Manuscripts Project between 2000 and 2008.

%prep
%setup -q -n gu5-510_ttf

%build

%install
install -d %{buildroot}%{fontdir}
install *.ttf %{buildroot}%{fontdir}

%files
%doc *.txt
%{fontdir}/*

%changelog
* Sun Dec 23 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 5.110
- Rebuilt for Fedora
