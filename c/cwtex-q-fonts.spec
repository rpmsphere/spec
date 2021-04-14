%define	fontdir	%{_datadir}/fonts/cwtex

Summary:	Improved cwTeX TrueType baseline fonts
Name:		cwtex-q-fonts
Version:	0.4
Release:	5.1
License:	GPLv2+ (OFL for *ZH)
Group:		User Interface/X
URL:		https://github.com/l10n-tw/cwtex-q-fonts
BuildArch:	noarch
Source:		%{name}-v04.tar.xz

%description
Those five TrueType fonts (ming,kai,fs,heib,yen face) are transformed
from cwTeX Traditional Chinese Type 1 fonts, and merge Alexej Kryukov's
CM-LGC font and Koanughi Un's Un-Fonts by Edward G.J. Lee.

Further improvements on Bobomofo are made since 2008 by Chen-Pan Liao.

%prep
%setup -q -n %{name}-v04

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{fontdir}
install -m 0644 *.ttf $RPM_BUILD_ROOT%{fontdir}

%post
[ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache 2> /dev/null

%postun
[ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache 2> /dev/null

%files
%doc README.md *.txt
%{fontdir}/*.ttf

%changelog
* Tue Mar 17 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
