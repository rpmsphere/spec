Name:           outwiker
Version:        1.6.0
Release:        3.1
License:        GPL-3.0
Summary:        Tree Notes Organizer
URL:            http://jenyay.net/Outwiker/English
Group:          Productivity/Office/Organizers
Source0:        http://jenyay.net/uploads/Soft/Outwiker/%{name}-%{version}-src.tar.gz
# PATCH-FIX-OPENSUSE outwiker-1.6.0-fonts.patch lazy.kent@opensuse.org -- don't use MS fonts
Patch0:         outwiker-1.6.0-fonts.patch
BuildArch:      noarch

%description
OutWiker is designed to store notes in a tree. Such programs are called
"outliner", personal wiki, or tree-like editors.

OutWiker's main difference from the other similar programs is keeping
the tree of notes in the form of directories on disk, and encouraging
changing the base by external sources and programs. Also any number of
files can be attached to the page. OutWiker can contain pages of
different types, currently supports two types of pages: plain text and
HTML, but the number of types of pages will increase in future.

%prep
%setup -q
%patch0

# Prepare *.py.
find src/%{name} -name \*.py -exec \
    sed -i 's/\r$//;/\/usr\/bin\/env/d;/\/usr\/bin\/python/d' '{}' \;
sed -i 's/\r$//' src/runoutwiker.py

# Prepare docs.
mv README README.russian
mv debian/README.Debian README

%build

%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_datadir}/%{name}/{copyright,README}
%find_lang %{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py
sed -i 's|^python |python2 |' %{buildroot}%{_bindir}/%{name}

%files -f %{name}.lang
%doc copyright README.russian README
%{_bindir}/%{name}
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/help/help_ru
%exclude %{_datadir}/%{name}/locale
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/%{name}/help/help_ru
%{_datadir}/%{name}/locale

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.0
- Rebuilt for Fedora
* Fri Jun  1 2012 lazy.kent@opensuse.org
- Initial package created - 1.6.0.
- Add outwiker-1.6.0-fonts.patch: don't use MS fonts.
