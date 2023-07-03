Name:          umb-scheme
Version:       3.2
Release:       18.1
Summary:       An implementation of the Scheme programming language
Group:         Development/Applications
URL:           https://www.cs.umb.edu/~wrc/scheme/
Source:        https://www.cs.umb.edu/~wrc/scheme/umb-scheme-%{version}.tar.gz
#Source1:       https://swissnet.ai.mit.edu/ftpdir/scm/slib2d5.zip
Source2:       slibcat
Patch0:        %{name}-3.2-misc.patch
Patch1:        %{name}-3.2-texinfo.patch
Patch2:        %{name}-3.2-config.patch
Patch3:        %{name}-3.2-man.patch
Patch4:        %{name}-3.2-chapter.patch
Patch5:        %{name}-3.2-slib2c7.patch
Patch6:        %{name}-3.2-share.patch
Patch7:        %{name}-3.2-vi.patch
License:       GPL
Requires:      slib

%description
UMB Scheme is a public domain implementation of the Scheme programming language.
Scheme is a statically scoped and properly tail-recursive dialect of the Lisp
programming language, designed with clear and simple semantics and a minimal
number of ways to form expressions.

%prep
%setup -q -n scheme-3.2
rm -fr slib
#unzip -q -o %{SOURCE1}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p1
%patch7 -p1
sed -i 's| @thistitle||' scheme.texinfo

%build
make
makeinfo scheme.texinfo

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_datadir}/%{name},%{_mandir}/man1}

install -m755 scheme $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m755 scheme.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/slibcat

find slib | cpio -pdm $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m644 prelude.scheme $RPM_BUILD_ROOT%{_datadir}/%{name}

install -m644 scheme.info $RPM_BUILD_ROOT%{_infodir}/%{name}.info
gzip -9nf $RPM_BUILD_ROOT%{_infodir}/%{name}.info

chmod -x $RPM_BUILD_ROOT%{_mandir}/*/*

# add symlink to slib
ln -s ../slib $RPM_BUILD_ROOT%{_datadir}/umb-scheme/slib

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %dir %{_datadir}/%{name}
%attr(0644,root,root) %{_datadir}/%{name}/prelude.scheme
%attr(0644,root,root) %{_datadir}/%{name}/slibcat
%attr(0644,root,root) %{_datadir}/%{name}/slib
#%attr(0755,root,root) %dir %{_datadir}/%{name}/slib
#%attr(0644,root,root) %{_datadir}/%{name}/slib/*
%{_mandir}/man1/%{name}.1*
%{_infodir}/%{name}.*
#%doc slib/ANNOUNCE slib/FAQ slib/README

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2
- Rebuilt for Fedora

* Tue Nov 06 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 3.2-4mamba
- require external slib and remove from package

* Mon Mar 27 2006 Stefano Cotta Ramusino <stefano.cotta@qilinux.it> 3.2-3qilnx
- specfile fixed and updated
- added info file patch 

* Mon Nov 15 2004 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it>3.2-2qilnx
- rebuilt and moved from devel-contrib repository to devel repository

* Sun Oct 24 2004 Matteo Bernasconi <voyagernm@virgilio.it>3.2-1qilnx
- first build
