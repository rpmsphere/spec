Name:           minised
Version:        1.15
Release:        2.1
Summary:        A smaller, cheaper, faster SED implementation
License:        BSD
URL:            http://exactcode.com/opensource/minised/
Source0:        http://dl.exactcode.de/oss/%{name}/%{name}-%{version}.tar.gz

%description
This is a smaller, cheaper, faster SED implementation. GNU used to use it, 
until they built their own sed around an extended regexp package. For 
embedded use we searched for a tiny sed implementation especially for use 
with the dietlibc and found Eric S. Raymond's sed implementation quite handy.
Though it suffered several bugs and was not under active maintenance anymore.
After sending a bunch of fixes we agreed to continue maintaining this 
lovely, historic sed implementation.

%prep
%setup -q

%build
%make_build CFLAGS="%{optflags} -Wwrite-strings" LDFLAGS="%{?__global_ldflags}"

%install
%make_install

%files
%doc LICENSE README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Oct 17 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.15
- Rebuild for Fedora
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Tue Jan 20 2015 Christopher Meng <rpm@cicku.me> - 1.15-1
- Update to 1.15
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Wed Apr 02 2014 Christopher Meng <rpm@cicku.me> - 1.14-4
- Fix for building with -Werror=format-security.
- SPEC cleanup.
- Harden the build.
- Insert LDFLAGS during building.
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Fri May 17 2013 Christopher Meng <rpm@cicku.me> - 1.14-2
- Add check test.
* Thu Feb 21 2013 Christopher Meng <rpm@cicku.me> - 1.14-1
- Initial package.
