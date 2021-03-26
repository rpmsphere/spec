%define theme_name Apparatus

Summary:        Apparatus cursor theme
Name:           apparatus-cursor-theme
Version:        20080612
Release:        3.1
License:        freeware
Group:          User Interface/Desktops
URL:            http://s0ury.deviantart.com/art/J-Aroche-s-G-A-Converted-88491633?q=1&qo=1
Source0:        http://www.deviantart.com/download/88491633/j_aroche__s_g_a__converted_by_s0ury.zip
BuildArch:      noarch

%description
This Cursor theme has been made by J.Aroche, it has been converted by me to
a X11 Cursor. Also included are 4 different versions, blue, green, red, yellow.
The 'busy' animation has been changed on all four versions, since the original
is too big and doesn't integrate well with compiz-fusion enabled.
Link to J.Aroche's original cursor:
http://aroche.deviantart.com/art/Green-Aparatus-71526723

%prep
%setup -q -c
tar xf Blue%{theme_name}.tar.gz
tar xf Green%{theme_name}.tar.gz
tar xf Red%{theme_name}.tar.gz
tar xf Yellow%{theme_name}2.tar.gz

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
cp -a Blue%{theme_name} Green%{theme_name} Red%{theme_name} Yellow%{theme_name}2 $RPM_BUILD_ROOT%{_datadir}/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/icons/*%{theme_name}*

%changelog
* Thu Dec 08 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20080612
- Rebuild for Fedora
