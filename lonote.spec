Name:           lonote
Version:        1.5.1
Release:        1
Summary:        Personal Notebook based on Qt Webkit
# The entire source code is GPLv3 except ./lonote/google_dmp/ which is ASL 2.0
License:        GPLv3 and ASL 2.0
URL:            http://code.google.com/p/lonote
#Source0:        http://lonote.googlecode.com/files/%{name}-%{version}.7z
Source0:	%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  dos2unix
Requires:       python3-PyQt4

%description
LoNote is a Note-Taking software based on Python3 and PyQt4. Each page is
saved in HTML format and the program is actually a WYSIWYG HTML editor
specialized for note-taking convenience.

%prep
%setup -q
sed -i -e '/^#!\//, 1d' lonote/google_dmp/diff_match_patch.py
sed -i -e '1i #coding=utf-8' lonote/__init__.py
sed -i -e '49d' setup.py

%build
LANG=zh_TW.UTF-8 python3 setup.py build

%install
rm -rf %{buildroot}
LANG=zh_TW.UTF-8 python3 setup.py install --root=%{buildroot} --skip-build

rm -r %{buildroot}%{_docdir}/%{name}/doc/{PO_FILE,localization.txt}
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
mv %{buildroot}%{_docdir}/%{name}/doc/* %{buildroot}%{_docdir}/%{name}-%{version}
rm -fr %{buildroot}%{_docdir}/%{name}/
dos2unix %{buildroot}%{_docdir}/%{name}-%{version}/*.txt

%find_lang %{name}

%files -f %{name}.lang
%{_docdir}/%{name}-%{version}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-*.egg-info
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*

%clean
rm -rf %{buildroot}

%changelog
* Mon Mar 12 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.1
- Rebuild for Fedora
* Sun Jan 22 2012 Robin Lee <cheeselee@fedoraproject.org>
- Initial package
