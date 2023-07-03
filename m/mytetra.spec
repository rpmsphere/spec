Name:           mytetra
Version:        1.30.1
Release:        7.1
License:        GPL-3.0
Summary:        Smart Manager for Information Collecting
URL:            https://webhamster.ru/site/page/index/articles/projectcode/138
Group:          Productivity/Office/Organizers
Source0:        https://webhamster.ru/db/data/articles/105/mytetra_1_30_1_src.zip
Source1:        https://webhamster.ru/db/data/articles/105/user_guide_ru.pdf
# PATCH-FIX-OPENSUSE mytetra-1.30-install.patch lazy.kent@opensuse.org -- fix install path
Patch0:         mytetra-1.30-install.patch
# PATCH-FIX-UPSTREAM mytetra-1.30.1-gcc47.patch lazy.kent@opensuse.org -- fix compilation with GCC 4.7
Patch1:         mytetra-1.30.1-gcc47.patch
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  unzip
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtNetwork)
BuildRequires:  pkgconfig(QtXml)

%description
MyTetra is an information collecting manager. It is a powerful program
for memorization data and structuring notes.
Capability:
- Infinite spreading tree for notes group.
- Arbitrary sorted notes in current branch.
- Arbitrary sorted branches in parent branch.
- Copy/Paste for notes and branches.
- Customizable trash for recovery lost data.
- WYSIWYG editor.

%package doc
Summary:        MyTetra User Guide
Group:          Documentation/Other
Provides:       locale(mytetra:ru)
BuildArch:      noarch

%description doc
MyTetra Russian user guide in PDF format.

%prep
%setup -qcn %{name}-%{version}
cp %{SOURCE1} .
%patch0
%patch1
chmod 644 desktop/any/mytetra.desktop

%build
qmake-qt4 \
    QMAKE_CFLAGS+="%{optflags}" \
    QMAKE_CXXFLAGS+="%{optflags}" \
    QMAKE_STRIP=""
make %{?_smp_mflags}

%install
make INSTALL_ROOT=$RPM_BUILD_ROOT install

%files
%doc readme.txt src/license.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*

%files doc
%doc user_guide_ru.pdf

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.30.1
- Rebuilt for Fedora
* Thu Apr 26 2012 lazy.kent@opensuse.org
- Patch to fix compilation with GCC 4.7.
- Use pkgconfig(*) as build dependencies.
- Removed check for unsupported openSUSE versions.
- Split off Russian user guide to subpackage.
* Thu Sep 15 2011 lazy.kent@opensuse.org
- Update to 1.30.1.
  * Fixed encryption/decryption bug in x86_64 systems.
- Updated "install" patch.
- Use icon_theme_cache_post/un macros.
- Added Russian User Guide to docs.
* Fri Jul 15 2011 lazy.kent@opensuse.org
- Downgrade to 1.28 because of error in encryption/decryption
  function in x86_64 systems.
* Wed Jul 13 2011 lazy.kent@opensuse.org
- Update to 1.30.
- "qtstring" patch to remove the redundant '::QString'.
- Updated "install" patch.
* Wed Mar 16 2011 lazy.kent@opensuse.org
- Initial package created - 1.28.
- Patch to fix install path.
