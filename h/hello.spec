Name:           hello
Version:        2.10
Release:        6.1
Summary:        Prints a Familiar, Friendly Greeting
Group:          Development/Tools
# Parts of the documentation are under GFDL, BSD, and Public Domain
# *All* code is GPLv3+.
License:        GPLv3+ and GFDL and BSD and Public Domain
URL:            http://www.gnu.org/software/hello/
Source0:        http://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz
BuildRequires: gettext help2man
Requires(post): info
Requires(preun): info

%description
Hello prints a friendly greeting. It also serves as a sample GNU
package, showing practices that may be useful for GNU projects.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%find_lang hello

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files -f hello.lang
%doc COPYING
%{_mandir}/man1/hello.1*
%{_bindir}/hello
%{_infodir}/hello.info*

%changelog
* Mon Aug 24 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.10
- Rebuild for Fedora
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Wed Jan 12 2011 Conrad Meyer <konrad@tylerc.org> - 2.6-1
- Bump to 2.6.
* Sun Mar 28 2010 Conrad Meyer <konrad@tylerc.org> - 2.5-1
- Bump version.
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Wed Dec 17 2008 Conrad Meyer <konrad@tylerc.org> - 2.4-1
- Initial package.
