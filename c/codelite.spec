%undefine _debugsource_packages
%global __prelink_undo_cmd %{nil}

Name:           codelite
Version:        17.0.0
Release:        1
License:        GPLv2+
Group:          Development/Tools
Summary:        CodeLite is a powerful open-source, cross platform code editor for C/C++
URL:            https://github.com/eranif/codelite
Source:         https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Requires:       libssh clang clang-tools-extra SDL
BuildRequires:  gcc gcc-c++ wxGTK-devel cmake clang-devel lldb-devel libssh-devel hunspell-devel sqlite-devel libXtst-devel
# Filter out these false-alarms from 'requires', as the package itself supplies them!
%{?filter_setup:
%filter_from_requires libcodeliteu.so; libpluginu.so; libwxscintillau.so; libwxsqlite3u.so;
%filter_setup
}

%description
CodeLite uses a sophisticated, yet intuitive interface which allows 
users to easily create, build and debug complex projects.

%prep
%setup -q -n %{name}-17.0
%ifarch aarch64
sed -i 's|SIGSTKSZ|8192|' sdk/codelite_cppcheck/cli/cppcheckexecutor.cpp
%endif
sed -i '168s|const||' Plugin/dtl/Diff.hpp
sed -i '62,77d' LiteEditor/editorsettingsdockingwidows.cpp

%build
mkdir -p build_release
export PATH=/usr/libexec/wxGTK:$PATH
# workaround for a pango/harfbuzz issue: see https://gitlab.kitware.com/cmake/cmake/issues/19531
(cd build_release && CXXFLAGS="-isystem /usr/include/harfbuzz -fPIC" cmake -G "Unix Makefiles" -DCOPY_WX_LIBS=1 -DAUTOGEN_REVISION=0 ..)
(cd build_release && make)

%install
%{__rm} -rf $RPM_BUILD_ROOT
(cd build_release && make DESTDIR=$RPM_BUILD_ROOT install)

# Avoid erroring out because fedora >29 doesn't want ambiguous python shebangs
sed -i "s|#!/usr/bin/python|#!/usr/bin/$(echo $(readlink -qn /usr/bin/python))|" %{buildroot}%{_bindir}/codelite_open_helper.py

# Create the .desktop on the fly, as it's not quite the same as the tarball one
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{name}
GenericName=C/C++ IDE
Comment=An IDE for creating C/C++ programs
Exec=%{name} %f
Icon=%{name}
Terminal=false
Type=Application
MimeType=application/x-codelite-workspace;application/x-codelite-project;
Categories=Development;
StartupNotify=false
Version=1.0
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/mime/packages/
cp -p %{name}.xml $RPM_BUILD_ROOT%{_datadir}/mime/packages/

#%define CL_ICON $RPM_BUILD_ROOT%{_datadir}/bitmaps/32-codelite-logo.png
#[16:31:45] <eranif1> ${CL_SRC_ROOT}/bitmaps/32-codelite-logo@2x.png
#[16:31:50] <eranif1> ${CL_SRC_ROOT}/bitmaps/32-codelite-logo.png
#[16:31:53] <eranif1> ${CL_SRC_ROOT}/bitmaps/64-codelite-logo@2x.png

#cp -p $RPM_BUILD_ROOT%{_datadir}/%{name}/images/cubes.png $RPM_BUILD_ROOT%{_datadir}/%{name}/images/codelite.png # Without this line, no icon was displayed in the kde menu or taskbar

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/mimetypes/
cp -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/codelite.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-%{name}-workspace.png
cp -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/codelite.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-%{name}-project.png

desktop-file-install  --delete-original       \
          --dir $RPM_BUILD_ROOT%{_datadir}/applications            \
                $RPM_BUILD_ROOT%{_datadir}/applications/codelite.desktop

%find_lang %{name}
mv %{buildroot}/usr/lib %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}/man1
cp Runtime/man1/*.1 %{buildroot}%{_mandir}/man1

%files -f %{name}.lang
%doc AUTHORS LICENSE COPYING 
%{_bindir}/*
%{_datadir}/codelite
%{_datadir}/applications/codelite.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_libdir}/%{name}
%{_mandir}/man1/*.1*

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 17.0.0
- Rebuilt for Fedora
* Wed Mar 03 2021 DH
- Added clang-tools-extra to Requires: to make LanguageServer code-completion work
* Wed Dec 30 2020 DH
- Corrected/simplified the .*Requires section
- Added SDL to Requires (see https://github.com/eranif/codelite/issues/2648)
* Wed Oct 30 2019 DH
- Compilation fixes for FC31 and wx3.1.3
* Wed May 08 2019 DH
- Updates for the CL 13 release
* Fri Nov 16 2018 DH
- Added build-requires for gcc/gcc-c++
* Fri May 05 2017 DH
- Patch for DnD freezes on Wayland
* Thu Jun 23 2016 DH
- Update for fedora24
* Fri Dec 04 2015 DH
- Update for icon change
* Wed Nov 04 2015 DH
- Fixes for fedora23 build
* Wed May 27 2015 DH
- Use the official wxGTK3 package for fedora22 builds
- Don't include the wx libs in the CL binary for fedora22
- Updated .*Requires accordingly
* Sat May 02 2015 DH
- Updated .*Requires and %%files as CL no longer supplies clang/lldb
* Thu Feb 05 2015 DH
- Updated %%files
* Tue May 13 2014 DH
- Added new files to %%files
- Updated BuildRequires (libedit)
* Fri Jan 10 2014 DH
- Added a new file to %%files
- Updated BuildRequires
* Sun Oct 20 2013 DH
- Added a new file to %%files
- Updated BuildRequires
* Thu Jul 11 2013 DH
- Added two new files to %%files
* Fri Mar 01 2013 DH
- Updated for the change to using cmake
* Wed Jan 23 2013 DH
- Additions for wxCrafter
* Wed Aug 29 2012 DH
- Added new binary codelitegcc to %%files
* Tue Nov 22 2011 DH
- Add libclang.so to the Requires filter
* Wed May 25 2011 DH
- Add filter for FC15 to remove the codelite-provided lib*.so from 'Requires'!
* Tue Jan 18 2011 DH
- Changes for mimetype stuff
* Fri Dec 24 2010 DH
- Use %%find_lang for translations
* Wed Mar 03 2010 DH
- Spec file: Added codelite_xterm
* Thu Sep 24 2009 DH
- Spec file: Added codelite_cppcheck
* Tue Feb 24 2009 DH
- Spec file: Corrected names. Disabled unwanted things in configure
* Tue Feb 24 2009 Jess Portnoy <kernel01@gmail.com> 1.0.2782-1
- Spec file: Added call to desktop-file-install and %%doc
  code: fixed perms and other rpmlint issues.
* Sat Feb 21 2009 Jess Portnoy <kernel01@gmail.com> 1.0.2781-1
- Reworked the rpm package to satisfy Fedora Core conventions.
