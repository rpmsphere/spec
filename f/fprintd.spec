Name:		fprintd
Version:	0.8.0
Release:	1%{?dist}
Summary:	D-Bus service for Fingerprint reader access

Group:		System Environment/Daemons
License:	GPLv2+
Source0:	http://freedesktop.org/~hadess/%{name}-%{version}.tar.xz
Url:		http://www.freedesktop.org/wiki/Software/fprint/fprintd
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    s390 s390x

BuildRequires:	dbus-glib-devel
BuildRequires:	pam-devel
BuildRequires:	libfprint-devel >= 0.1.0
BuildRequires:	polkit-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:  autoconf automake libtool
BuildRequires:	perl-podlators

%description
D-Bus service to access fingerprint readers.

%package pam
Summary:	PAM module for fingerprint authentication
Requires:	%{name} = %{version}-%{release}
# Note that we obsolete pam_fprint, but as the configuration
# is different, it will be mentioned in the release notes
Provides:	pam_fprint = %{version}-%{release}
Obsoletes:	pam_fprint < 0.2-3
Requires(postun): authconfig

Group:		System Environment/Base
License:	GPLv2+

%description pam
PAM module that uses the fprintd D-Bus service for fingerprint
authentication.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Group:		Development/Libraries
License:	GFDLv1.1+
BuildArch:	noarch

%description devel
Development documentation for fprintd, the D-Bus service for
fingerprint readers access.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --libdir=/%{_lib}/ --enable-gtk-doc --enable-pam

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/lib/fprint

rm -f $RPM_BUILD_ROOT/%{_lib}/security/pam_fprintd.{a,la,so.*}

%find_lang %{name}

%postun pam
if [ $1 -eq 0 ]; then
  /sbin/authconfig --disablefingerprint --update || :
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README COPYING AUTHORS TODO
%{_bindir}/fprintd-*
%{_libexecdir}/fprintd
# FIXME This file should be marked as config when it does something useful
%{_sysconfdir}/fprintd.conf
%{_sysconfdir}/dbus-1/system.d/net.reactivated.Fprint.conf
%{_datadir}/dbus-1/system-services/net.reactivated.Fprint.service
/usr/lib/systemd/system/fprintd.service
%{_datadir}/polkit-1/actions/net.reactivated.fprint.device.policy
%{_localstatedir}/lib/fprint
%{_mandir}/man1/fprintd.1.gz

%files pam
%defattr(-,root,root,-)
%doc pam/README
/%{_lib}/security/pam_fprintd.so

%files devel
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/
%{_datadir}/dbus-1/interfaces/net.reactivated.Fprint.Device.xml
%{_datadir}/dbus-1/interfaces/net.reactivated.Fprint.Manager.xml

%changelog
* Wed Sep 13 2017 Bastien Nocera <bnocera@redhat.com> - 0.8.0-1
+ fprintd-0.8.0-1
- Update to 0.8.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 09 2017 Bastien Nocera <bnocera@redhat.com> - 0.7.0-2
+ fprintd-0.7.0-2
- Fix fprintd-pam being disabled after upgrade (#1398371)

* Wed Oct 12 2016 Bastien Nocera <bnocera@redhat.com> - 0.7.0-1
+ fprintd-0.7.0-1
- Update to 0.7.0

* Thu Sep 22 2016 Bastien Nocera <bnocera@redhat.com> - 0.6.0-5
- Fix warning when uninstalling fprintd-pam (#1203671)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.6.0-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Tue Feb 03 2015 Bastien Nocera <bnocera@redhat.com> 0.6.0-1
- Update to 0.6.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 11 2013 Bastien Nocera <bnocera@redhat.com> 0.5.1-1
- Update to 0.5.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 05 2013 Bastien Nocera <bnocera@redhat.com> 0.5.0-1
- Update to 0.5.0

* Tue Feb 19 2013 Bastien Nocera <bnocera@redhat.com> 0.4.1-5
- Co-own the gtk-doc directory (#604351)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Bastien Nocera <bnocera@redhat.com> 0.4.1-1
- Update to 0.4.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 09 2010 Ray Strode <rstrode@redhat.com> 0.2.0-2
- Don't allow pam module to ever get unmapped, since that causes
  crashes in dbus-glib, gobject, etc.

* Thu Aug 19 2010 Bastien Nocera <bnocera@redhat.com> 0.2.0-1
- Update to 0.2.0

* Wed Dec 09 2009 Bastien Nocera <bnocera@redhat.com> 0.1-16.git04fd09cfa
- Remove use of g_error(), or people think that it crashes when we actually
  abort() (#543194)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-15.git04fd09cfa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Bastien Nocera <bnocera@redhat.com> 0.1-14.git04fd09cfa
- Merge polkit patch and fix for polkit patch

* Tue Jul 21 2009 Bastien Nocera <bnocera@redhat.com> 0.1-13.git04fd09cfa
- Make the -devel package noarch (#507698)

* Thu Jul  9 2009 Matthias Clasen <mclasen@redhat.com> 0.1-12.git04fd09cfa
- Fix the pam module (#510152)

* Sat Jun 20 2009 Bastien Nocera <bnocera@redhat.com> 0.1-11.git04fd09cfa
- Remove obsolete patch

* Tue Jun 9 2009 Matthias Clasen <mclasen@redhat.com> 0.1-10.git04fd09cfa
- Port to PolicyKit 1

* Thu May 07 2009 Bastien Nocera <bnocera@redhat.com> 0.1-9.git04fd09cfa
- Add /var/lib/fprint to the RPM to avoid SELinux errors (#499513)

* Tue Apr 21 2009 Karsten Hopp <karsten@redhat.com> 0.1-8.git04fd09cfa.1
- Excludearch s390 s390x, as we don't have libusb1 on mainframe, we can't build
  the required libfprint package

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8.git04fd09cfa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 - Bastien Nocera <bnocera@redhat.com> - 0.1-7.git04fd09cfa
- Add a patch to handle device disconnects

* Mon Jan 26 2009 - Bastien Nocera <bnocera@redhat.com> - 0.1-6.git04fd09cfa
- Update to latest git, fixes some run-time warnings

* Wed Dec 17 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1-5.git43fe72a2aa
- Add patch to stop leaking a D-Bus connection on failure

* Tue Dec 09 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1-4.git43fe72a2aa
- Update D-Bus config file for recent D-Bus changes

* Thu Dec 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1-3.git43fe72a2aa
- Update following comments in the review

* Sun Nov 23 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1-2.gitaf42ec70f3
- Update to current git master, and add documentation

* Tue Nov 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1-1
- First package

