%define theme_name Matrix

Summary: Matrix for GNOME environment
Name: matrix-gnome-theme
Version: 20100410
Release: 11.1
License: GPL
Group: User Interface/Desktops
Source0: HLMatrix.tar.gz
Source1: Matrix-index.theme
Source2: matrix_ver_1.0.tar.gz
Source3: matrix-wallpapers.tar.gz
BuildArch: noarch
URL: http://gnome-look.org/content/show.php/Pwnage+Matrix+Conversion+Pack?content=123039
Requires: nostromo-icon-theme
Requires: pulseglass-cursor-theme
Requires: industrial-gnome-theme

%description
The full gnome theme inspired by the movie "The Matrix" (1999).
GTK theme: Human Login theme, with custom colours.
Wallpaper: From gnome-look as well.
GDM theme: The Matrix from gnome-look, made by NoGe.

%prep
%setup -q -c -a 2 -a 3
rm -f `find . -name '*~'`

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/HLMatrix
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gdm/%{theme_name}
cp -a matrix_ver_1.0/* $RPM_BUILD_ROOT%{_datadir}/gdm/%{theme_name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/%{theme_name}
cp -a wallpapers/* $RPM_BUILD_ROOT%{_datadir}/backgrounds/%{theme_name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cp -a HLMatrix $RPM_BUILD_ROOT%{_datadir}/themes
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/HLMatrix/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/HLMatrix
%{_datadir}/gdm/Matrix
%{_datadir}/backgrounds/Matrix

%changelog
* Thu May 19 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20100410
- Rebuild for Fedora
