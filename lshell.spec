Name:           lshell
Version:        0.9.18
Release:        8
Summary:        A Python-based limited shell
License:        GPLv3+
URL:            https://github.com/ghantoos/lshell
Source0:        https://github.com/ghantoos/lshell/releases/download/%{version}/%{name}_%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
Requires(pre):  shadow-utils

%description
lshell provides a limited shell configured per user. The configuration
is done quite simply using a configuration file.

%prep
%setup -q
#Fix permission
chmod -x CHANGES

%build
%py3_build

%install
%py3_install
# Doc files at the wrong place
rm %{buildroot}%{_defaultdocdir}/lshell/{CHANGES,COPYING,README.md}

%pre
getent group lshell >/dev/null || groupadd -r lshell

%post
grep -q '^%{_bindir}/%{name}$' %{_sysconfdir}/shells || \
    echo '%{_bindir}/%{name}' >> %{_sysconfdir}/shells

%postun
if [ $1 -eq 0 ]; then
    sed -i '/^\/%{_bindir}\/%{name}$/d' %{_sysconfdir}/shells
fi

%files
%doc CHANGES README.md
%license COPYING
%{_mandir}/man*/*.*
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{python3_sitelib}/lshell/
%{python3_sitelib}/%{name}*.egg-info

%changelog
* Fri Dec 06 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.18
- Rebuild for Fedora
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.18-7
- Rebuilt for Python 3.7
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.18-3
- Rebuild for Python 3.6
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.18-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages
* Thu May 05 2016 Lumír Balhar <frenzy.madness@gmail.com> - 0.9.18-1
- Updated to new upstream version 0.9.18 (rhbz#1323254)
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Sat Nov 14 2015  Fabian Affolter <mail@fabian-affolter.ch> - 0.9.17-2
- Switch to Python3
* Wed Oct 28 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.17-1
- Updated to new upstream version 0.9.17
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Wed Oct 29 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.16-4
- Add to shells (rhbz#1111074)
* Wed Oct 29 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.16-3
- Add group (rhbz#1109511)
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sun Sep 08 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.16-1
- Updated to new upstream version 0.9.16
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Wed Jun 26 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.15.1-4
- Spec file updated
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Mon Mar 19 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.15.1-1
- Updated to new upstream version 0.9.15.1
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Wed Nov 10 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.14-1
- Updated to new upstream version 0.9.14
* Sun Oct 17 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.13-1
- Updated to new upstream version 0.9.13
* Fri Jul 30 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild
* Sat Jul 03 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.12-2
- Removed setuptools
- Marked log file as config
* Sun Jun 06 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.12-1
- Added logging support
- Updated macros
- Updated to new upstream version 0.9.12
* Mon Mar 15 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.10-1
- Updated to new upstream version 0.9.10
* Sun Mar 07 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.9-1
- Removed compression format from man page
- Updated to new upstream version 0.9.9
* Sun Dec 20 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.8-1
- Updated to new upstream version 0.9.8
* Thu Nov 26 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.7-1
- Updated to new upstream version 0.9.7
* Fri Aug 14 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.5-1
- Updated to new upstream version
* Tue Jul 07 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.4-1
- Updated to new upstream version 0.9.4
* Wed Apr 15 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-1
- Initial package for Fedora
