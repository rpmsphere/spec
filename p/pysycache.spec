Name:           pysycache
Summary:        Educational point-and-click software for young children
Version:        3.1c
Release:        7.1
Group:          Applications/Education
URL:            https://www.pysycache.org/
License:        GPL, GPLv2
Source0:        https://download.tuxfamily.org/py4childs/pysycache/v3.1/%{name}-src-%{version}.zip
Patch0:         pysycache-desktop.patch
Patch1:         pysycache-lang-de.patch
Patch2:         pysycache-lang-es.patch
Patch3:         pysycache-console_encoding.patch
Patch4:         pysycache-fast_quitting.patch
Patch5:         pysycache-no-return-in-nonvoid-function.patch
BuildArch:      noarch
%description
PySyCache is an educational software for the young children (4-7 years old)
with target to learn them to move the mouse to click with mouse buttons
PySyCache doesn't want some powerful computer, and it can be used
at home with yours children in the schools.

Author:
-------
    Vincent DEROO <contact.pysycache(AT)free.fr>

%prep
%setup -q -n %{name}-src
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
cat << EOF > %{name}.sh
#!/bin/bash
cd %{_datadir}/%{name}
exec python pysycache.py \$@
EOF

%install
# python files
install -d %{buildroot}%{_datadir}
cp -a pysycache %{buildroot}/%{_datadir}
# executable
install -Dm755 pysycache.sh %{buildroot}/%{_bindir}/%{name}
# documentation
install -d %{buildroot}%{_defaultdocdir}/%{name}
cp -a pysycache/doc/* %{buildroot}%{_defaultdocdir}/%{name}/
for i in AUTHORS ChangeLog COPYING NEWS README; do
	mv %{buildroot}%{_datadir}/%{name}/$i %{buildroot}%{_defaultdocdir}/%{name}
done
rm %{buildroot}%{_datadir}/%{name}/INSTALL
# man files
install -Dm644 linux/man/pysycache.1 %{buildroot}%{_mandir}/man1/pysycache.1
# desktop entry
install -d %buildroot/%{_datadir}/pixmaps
install -d %buildroot/%{_datadir}/applications
install -m 644 linux/usr/share/pixmaps/*.png %buildroot/%{_datadir}/pixmaps/
install -m 644 linux/usr/share/applications/*.desktop %buildroot/%{_datadir}/applications/
# configuration directory
install -d %buildroot/%{_sysconfdir}/pysycache
install -m644 linux/etc/pysycache/pysycache.dfg %buildroot/%{_sysconfdir}/pysycache/
mkdir -p %{buildroot}/var/games/%{name}/{users,themes-move,themes-click,themes-dblclick,themes-buttons,themes-puzzle}

%clean
rm -rf %buildroot

%files
%doc %{_defaultdocdir}/%{name}
%{_bindir}/%{name}
%dir %{_sysconfdir}/pysycache
%config(noreplace) %{_sysconfdir}/pysycache/pysycache.dfg
%{_datadir}/%{name}
%{_mandir}/man1/pysycache.1.*
%{_datadir}/applications/pysycache-admin.desktop
%{_datadir}/applications/pysycache.desktop
%{_datadir}/pixmaps/%{name}.png
/var/games/%name

%changelog
* Sun Mar 24 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1b
- Rebuilt for Fedora
* Tue Dec 27 2011 lars@linux-schulserver.de
- use games user and games group for pysycache from now on
- use verify scripts during install and for rpm verify
- compile the single C-file directly with optargs instead of
  using make
- added patches:
  + pysycache-console_encoding.patch
  + pysycache-fast_quitting.patch
  + pysycache-no-return-in-nonvoid-function.patch
* Wed Nov  5 2008 lars@linux-schulserver.de
- enable post-build-checks again: it's an rpmlint check now
* Thu Oct 30 2008 lars@linux-schulserver.de
- disable post-build-checks
* Tue Oct 14 2008 lars@linux-schulserver.de
- update to 3.1b (3.1.01)
- patches adapted
* Thu Sep 25 2008 lars@linux-schulserver.de
- moved to Education base repository
* Sun May 18 2008 lars@linux-schulserver.de
- added /var/games/pysycache/themes-dblclick (os-edu #0000035)
* Mon Mar 17 2008 lars@linux-schulserver.de
- just specfile beautify
* Mon Aug  6 2007 lars@linux-schulserver.de
- added /etc/pysycache to permissions file
- added themes-move from older release (missing theme will crash
  pysycache)
* Sun Aug  5 2007 lars@linux-schulserver.de
- added pysycache-rpmlintrc to avoid some warnings
- using fdupes to save space
- added pysycache-lang-de.patch to correct some german spelling
- use the compiled pysycache binary => package is arch dependend
- added permissions file for config, and /var/games/pysycache
  directory
* Sat Aug  4 2007 lars@linux-schulserver.de
- initial version 3.0.1
