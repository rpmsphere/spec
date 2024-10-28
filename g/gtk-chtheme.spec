Name:           gtk-chtheme
Version:        0.3.1
Release:        19.1
Summary:        Gtk+ 2.0 theme preview and selection made slick
Group:          User Interface/Desktops
License:        GPLv2+
URL:            https://plasmasturm.org/programs/gtk-chtheme/
Source0:        https://plasmasturm.org/code/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         %{name}-nostrip.patch
Patch1:         %{name}-0.3.1-new-api.patch
Patch2:         %{name}-0.3.1-fix.patch
BuildRequires:  gtk2-devel desktop-file-utils

%description
As the name suggests, this little program lets you change your Gtk+ 2.0 theme.
The aim is to make theme preview and selection as slick as possible. Themes
installed on the system are presented for selection and previewed on the fly.
A large variety of widgets provides a comprehensive demonstration.

%prep
%setup -q
%patch 0 -p0 -b .orig
%patch 1 -p1 -b .orig
%patch 2 -p1 -b .fix

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

desktop-file-install                                    \
        --dir=%{buildroot}%{_datadir}/applications      \
        %{SOURCE1}

# Fix permission of man file
find %{buildroot}%{_mandir}/man1/%{name}.* -type f | xargs chmod 0644 || true
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc ChangeLog COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.*
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Apr 14 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Thu Mar 22 2012 Tom Callaway <spot@fedoraproject.org> - 0.3.1-10
- fix compile
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3.1-8
- Rebuild for new libpng
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Thu Jul 15 2010 German A. Racca <gracca@gmail.com> - 0.3.1-6
- Fixed permission of man file the right way
* Wed Jul 14 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.3.1-5
- Add patch to build with newer gtk
* Thu Jun 17 2010 German A. Racca <gracca@gmail.com> 0.3.1-4
- Fixed permission of man file
* Wed Jun 16 2010 German A. Racca <gracca@gmail.com> 0.3.1-3
- Rebuilt for Fedora 13
* Tue May 04 2010 German A. Racca <gracca@gmail.com> 0.3.1-2
- Added %%{dist} tag
- Added patch for not stripping the binary file
* Mon Mar 22 2010 German A. Racca <gracca@gmail.com> 0.3.1-1
- Initial release of RPM package
