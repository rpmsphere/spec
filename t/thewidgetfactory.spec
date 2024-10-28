Name:           thewidgetfactory
Version:        0.2.1
Release:        27.1
Summary:        A tool for previewing GTK widgets
Group:          Development/Tools
License:        GPL+
URL:            https://www.stellingwerff.com/?page_id=10 
Source0:        https://www.stellingwerff.com/TheWidgetFactory/%{name}-%{version}.tar.gz
Source1:        thewidgetfactory.desktop
Source2:        thewidgetfactory.png
Patch0:             thewidgetfactory-aarch64.patch
BuildRequires:  gtk2-devel, desktop-file-utils, libcap-devel

%description
The Widget Factory is a program designed to show a wide range of widgets
on a single window.

%prep
%setup -q
%patch 0 -p1 -b .thewidgetfactory-aarch64
sed -i '1i #include <string.h>' src/themes.c

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        %{SOURCE1}
install -Dm644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png

%files
%doc ChangeLog README COPYING
%{_bindir}/twf
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Jun 03 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1
- Rebuilt for Fedora
* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Fri Aug 16 2013 Luya Tshimbalanga <luya@fedoraproject.org> - 0.2.1-18
- Patch to support aarch64
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Fri Feb 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2.1-16
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077
* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2.1-12
- Rebuild for new libpng
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.2.1-8
- fix license tag
* Fri Feb 22 2008 Luya Tshimbalanga <luya_tfz@thefinalzone.com> - 0.2.1-7
- Added libcap-devel for dependancy
* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.1-6
- Autorebuild for GCC 4.3
* Fri Jan 18 2008 Luya Tshimbalanga <luya_tfz@thefinalzone.com> 0.2.1-5
 - Rebuilt for dependencies
* Tue Aug 21 2007 Luya Tshimbalanga <luya_tfz@thefinalzone.com> 0.2.1-4.1
 - Renamed GPL to GPL+ following the new Fedoa tagging license schema
 - Removed tools name in Categories from desktop file
 - Removed Version in desktop file
* Sat Oct 21 2006 Luya Tshimbalanga <luya_tfz@thefinalzone.com> 0.2.1-2
 - Fixed permission on bin directory
 - Added desktop-file-utils for menu
* Fri Oct 20 2006 Luya Tshimbalanga <luya_tfz@thefinalzone.com> 0.2.1-1
 - Initial creation 
