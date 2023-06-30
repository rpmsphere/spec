%define	fontdir	%{_datadir}/fonts/hannom

Summary: Chinese and Vietnamese TrueType fonts
Name: hannom-fonts
Version: 2005
Release: 3.1
License: free, non-profit
Group: User Interface/X
BuildArch: noarch
Source0: https://sourceforge.net/projects/vietunicode/files/hannom/hannom%20v2005/hannom.zip
Source1: COPYING-%name
URL: https://vietunicode.sourceforge.net/fonts/fonts_hannom.html
Requires(post): fontconfig

%description
The true type fonts HAN NOM A and HAN NOM B have been developed by Chan Nguyen
Do Quoc Bao (Germany), To Minh Tam (USA) and Ni sinh Thien Vien Vien Chieu
(Vietnam). Their work got started in 2001, completed in 2003, and publicized
in 2005. These two true type fonts can be used with WIN-2000 or WIN-XP and
Office XP or Office 2003 to display Han and Nom characters with code points
by the Unicode Standard. This set of true type fonts is available with low
resolution.

%prep
%setup -q -c
cp %{SOURCE1} COPYING

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{fontdir}
install -m 0644 *.ttf %{buildroot}%{fontdir}

%clean
rm -rf %{buildroot}

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%doc COPYING
%{fontdir}/*

%changelog
* Sun Jun 09 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2005
- Rebuilt for Fedora
