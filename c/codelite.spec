%global debug_package %{nil}

Name:           codelite
Version:        15.0
Release:        1
License:        GPLv2+
Group:          Development/Tools
Summary:        CodeLite is a powerful open-source, cross platform code editor for C/C++
URL:            http://codelite.sourceforge.net
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	wxGTK3-devel cmake libssh-devel hunspell-devel libedit-devel sqlite-devel
Requires:       libedit-devel

# Needed to prevent cpio "digest mismatch" errors when trying to install an rpm that incorporates 
# already-prelinked .so libs. See http://www.redhat.com/archives/rhl-devel-list/2009-December/msg00813.html
%global __prelink_undo_cmd %{nil}

# Filter out these false-alarms from 'requires', as the package itself supplies them!
#{?filter_setup:
#filter_from_requires libcodeliteu.so; libpluginu.so; libwxscintillau.so; libwxsqlite3u.so; libclang.so
#filter_setup
#}

%description
CodeLite uses a sophisticated, yet intuitive interface which allows 
users to easily create, build and debug complex projects.

%prep
%setup -q
sed -i 's/CL_WX_CONFIG wx-config/CL_WX_CONFIG wx-config-3.0/' CMakeLists.txt

%build
mkdir -p build_release
(cd build_release && cmake -G "Unix Makefiles" -DCMAKE_CXX_FLAGS="-I/usr/include/harfbuzz" -DwxWidgets_CONFIG_EXECUTABLE:FILEPATH=/bin/wx-config-3.0 -DCOPY_WX_LIBS=1 -DAUTOGEN_REVISION=0 ..)

(cd build_release && make %{?_smp_mflags})

%install
%{__rm} -rf $RPM_BUILD_ROOT
(cd build_release && make DESTDIR=$RPM_BUILD_ROOT install)

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

#mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/mimetypes/
#cp -p $RPM_BUILD_ROOT%{_datadir}/%{name}/images/cubes.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-%{name}-workspace.png
#cp -p $RPM_BUILD_ROOT%{_datadir}/%{name}/images/cubes.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/mimetypes/application-x-%{name}-project.png

%find_lang %{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc AUTHORS LICENSE COPYING 
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_libdir}/%{name}
%{_mandir}/man1/%{name}*

%post
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%changelog
* Sun Apr 4 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 15.0
- Rebuild for Fedora
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
- Reworked the rpm package to satisfy Fedora Core conventions
