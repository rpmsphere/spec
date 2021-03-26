Name:		xsettingsd
Version:	0
%define commit_id 7804894
Release:	0.17.20091208git%{commit_id}
Summary:	Provides settings to X11 clients via the XSETTINGS specification
License:	BSD
URL:		http://code.google.com/p/xsettingsd/
# from http://github.com/derat/xsettingsd/tarball/%{commid_id}
Source0:	derat-xsettingsd-%{commit_id}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:	python3-scons libstdc++-devel libX11-devel

%description
xsettingsd is a daemon that implements the XSETTINGS specification.

It is intended to be small, fast, and minimally dependent on other libraries.
It can serve as an alternative to gnome-settings-daemon for users who are not
using the GNOME desktop environment but who still run GTK+ applications and
want to configure things such as themes, font anti-aliasing/hinting, and UI
sound effects.

%prep
%setup -q -n derat-%{name}-%{commit_id}
sed -i -e "s|-Wall -Werror|%{optflags}|g" -e "s|print \(.*\)|print(\1)|" SConstruct

%build
scons

%install
install -Dm0755 xsettingsd		%{buildroot}%{_bindir}/xsettingsd
install -Dm0755 dump_xsettings		%{buildroot}%{_bindir}/dump_xsettings
install -Dm0644 xsettingsd.1		%{buildroot}%{_mandir}/man1/xsettingsd.1
install -Dm0644 dump_xsettings.1	%{buildroot}%{_mandir}/man1/dump_xsettings.1

%files
%{_bindir}/*
%{_mandir}/man1/*
%doc README COPYING

%changelog
* Tue Dec 08 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0
- Rebuild for Fedora
* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-0.9.20091208git7804894
- Rebuilt for GCC 5 C++11 ABI change
* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.20091208git7804894
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Fri Oct 29 2010 Pierre Carrier <prc@redhat.com> 0-0.1.20091208git7804894
- Initial packaging
