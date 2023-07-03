Name:           smarteiffel
Version:        2.4
Release:        11.1
Summary:        The GNU Eiffel Compiler and Libraries
Group:          Development/Languages
License:        GPLv2+
URL:            https://smarteiffel.loria.fr
Source0:        %{name}.tgz
Source1:        SmartEiffel.serc
BuildRequires:  libX11-devel
BuildRequires:  mesa-libGL-devel

%description
SmartEiffel is a small, portable implementation of the Eiffel OO
programming language.  Eiffel cleanly implements all the important
concepts of OO programming, including: multiple inheritance,
genericity, polymorphism, and encapsulation.  Eiffels unique feature
is Design By Contract, which increases the reusability and reliability
of program modules.

%undefine _debugsource_packages

%prep
%setup -q -n SmartEiffel
sed -i 's|/usr/local|%{buildroot}/usr|' configure make_release.sh

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
#make_install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -f bin/se $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/SmartEiffel
for i in ace_check class_check clean compile compile_to_c finder pretty short eiffeldoc
do
    cp -f bin/$i $RPM_BUILD_ROOT%{_libexecdir}/SmartEiffel
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/SmartEiffel
for i in sys lib tools short tutorial
do
    cp -fr $i $RPM_BUILD_ROOT%{_datadir}/SmartEiffel
done

#mkdir -p $RPM_BUILD_ROOT%{_datadir}/SmartEiffel/man
#cp -fr man/*.txt $RPM_BUILD_ROOT%{_datadir}/SmartEiffel/man

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
sed -e "s|LIBDIR|%{_datadir}|; s|BINDIR|%{_bindir}|; s|LIBEXECDIR|%{_libexecdir}|; s|@RPM_OPT_FLAGS@|%se_rpm_opt_flags|" %{SOURCE1} > $RPM_BUILD_ROOT%{_sysconfdir}/serc

find $RPM_BUILD_ROOT%{_datadir}/SmartEiffel -name '.#*' -exec rm -f '{}' ';'
find $RPM_BUILD_ROOT%{_datadir}/SmartEiffel -type f -exec chmod 0644 '{}' ';'
find $RPM_BUILD_ROOT%{_datadir}/SmartEiffel -name '*.SH' -exec chmod 0755 '{}' ';'
#find www/papers -name '*.pdf.gz' -exec rm -f '{}' ';'
#find www/papers -name '*.ps*' -exec rm -f '{}' ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc READ_ME.txt GNU_LICENSE contrib misc
%{_bindir}/se
%{_datadir}/SmartEiffel
%{_libexecdir}/SmartEiffel
%config %{_sysconfdir}/serc

%changelog
* Fri Sep 21 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4
- Rebuilt for Fedora
* Sun Jan  6 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.3-2
- added buildreq libX11-devel
* Sat Jan  5 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.3-1
- new release 2.3
* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2.2-6
- rebuilt for unwind info generation, broken in gcc-4.1.1-21
* Fri Sep 22 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.2-5
- split off -doc subpackage
* Sun Jun 18 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.2-4
- disable creation of debuginfo package
* Wed Jan 18 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.2-3
- new version 2.2
* Mon Nov  7 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.2-1.beta5
- New Version 2.2.beta5
* Fri Aug  5 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.2-1.beta2
- New Version 2.2.beta2
* Fri Jun 24 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.2-1.beta1.2
- Some reordering of executables
* Fri Jun 17 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.2-1.beta1
- New Version 2.2beta1
* Tue Mar  8 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.1-1
- New Version 2.1
* Tue Oct  5 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:2.0-0.fdr.1
- New Version 2.0
* Mon Nov  3 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:1.1-0.fdr.1
- First Fedora release
