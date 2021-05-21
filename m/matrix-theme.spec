%define theme_name Matrix

Summary: Matrix for GNOME environment
Name: matrix-theme
Version: 20100410
Release: 11.1
License: GPL
Group: User Interface/Desktops
Source0: HLMatrix.tar.gz
Source1: Matrix-index.theme
Source2: matrix_ver_1.0.tar.gz
Source3: matrix-wallpapers.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
URL: http://gnome-look.org/content/show.php/Pwnage+Matrix+Conversion+Pack?content=123039

%description
Themes inspired by the movie "The Matrix" (1999).

%package -n hlmatrix-gnome-theme
Summary: Human Login GTK & Metacity theme

%description -n hlmatrix-gnome-theme
Human Login theme, with custom colours.

%package -n matrix-backgrounds
Summary: Matrix backgrounds

%description -n matrix-backgrounds
Wallpapers from gnome-look.

%package -n matrix-gdm-theme
Summary: Matrix GDM theme

%description -n matrix-gdm-theme
Matrix GDM theme from gnome-look, made by NoGe.

%prep
%setup -q -c -a 2 -a 3
rm -f `find . -name '*~'`

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/HLMatrix
cp -f %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/HLMatrix/index.theme
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gdm/%{theme_name}
cp -a matrix_ver_1.0/* $RPM_BUILD_ROOT%{_datadir}/gdm/%{theme_name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/%{theme_name}
cp -a wallpapers/* $RPM_BUILD_ROOT%{_datadir}/backgrounds/%{theme_name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cp -a HLMatrix $RPM_BUILD_ROOT%{_datadir}/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files -n hlmatrix-gnome-theme
%defattr(-,root,root,-)
%{_datadir}/themes/HLMatrix

%files -n matrix-gdm-theme
%defattr(-,root,root,-)
%{_datadir}/gdm/Matrix

%files -n matrix-backgrounds
%defattr(-,root,root,-)
%{_datadir}/backgrounds/Matrix

%changelog
* Thu May 19 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20100410
- Rebuilt for Fedora
