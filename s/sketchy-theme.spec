%define theme_name Sketchy

Summary: A pencil-drawn theme
Name: sketchy-theme
Version: 0.80
Release: 11.1
License: GPL
Group: User Interface/Desktops
Source0: http://www.deviantart.com/download/175492975/sketchy_by_therealpadster.zip
Source1: https://raw.githubusercontent.com/revdancatt/FutureLearn-Creative-Coding/master/week_05/c03_sketchy_hex_pattern/c03_sketchy_hex_pattern.jpg
Requires: nerdy-lines-icon-theme
Requires: sketch-cursor-theme
BuildArch: noarch
URL: http://therealpadster.deviantart.com/art/Sketchy-175492975

%description
The base was The_Rob's slickness, because it is very complete
and I want to have a full Sketchy desktop when I'm done.

%prep
%setup -q -n Sketchy
sed -i -e 's|Humanity|Nerdy-Lines|' -e 's|artwiz|sketch|' index.theme
echo BackgroundImage=/usr/share/themes/Sketchy/c03_sketchy_hex_pattern.jpg >> index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a * %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
chmod -x $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Fri May 27 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.80
- Rebuild for Fedora
