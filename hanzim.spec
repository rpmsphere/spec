%global debug_package %{nil}
Name: hanzim
Version: 1.3
Release: 1
Source: ftp://zakros.ucsd.edu/arobert/Chinese/%{name}-%{version}.tgz
Source1: %{name}.png
Patch: hanzim-makefilepaths.patch
License: GPL
Group: Applications/Education
Summary: A Chinese character learning-aid program
URL: http://hanzim.com/
BuildRequires: tk-devel
Requires: xorg-x11-fonts-misc, tk

%description
Hanzi Master ("Hanzim") is a program to aid in learning
(traditional or simplified) Chinese characters by Adrian Robert.

%prep
%setup -n Hanzim
%patch
sed -i -e 's/hanzigb16st/hanzigb24st/' -e 's/taipei16/hanzigb24st/' Data/fonts.unix    
sed -i '62i #define USE_INTERP_RESULT' hanzim.h

%build
make

%install
rm -fr $RPM_BUILD_ROOT
/bin/mkdir -p $RPM_BUILD_ROOT%{_bindir}
/bin/mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
make INSTALLROOT=$RPM_BUILD_ROOT/usr MANDIR=$RPM_BUILD_ROOT%{_mandir} install

# icons
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__cp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# freedesktop.org menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Type=Application
Name=Hanzi Master
Name[zh_TW]=漢字大師
Comment=A Chinese character learning-aid program
Comment[zh_TW]=中文字輔助學習程式
Exec=hanzim
Icon=hanzim
Terminal=false
Categories=Application;Education;
EOF

%post
##/usr/bin/hanzim -buildDB

%files
%doc CHANGES COPYING README TODO hanzim.doc
%{_bindir}/hanzim
%{_mandir}/man1/hanzim.1*
/usr/lib/Hanzim
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%clean
rm -fr $RPM_BUILD_ROOT

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuild for Fedora
* Thu Apr 11 2002 David Jao <djao@dominia.org>
- Initial package
