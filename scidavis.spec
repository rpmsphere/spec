%global pluginversion 1.0.0

Name:           scidavis
Version:        1.14
Release:        1
Summary:        Application for Scientific Data Analysis and Visualization

License:        GPLv2+ and GPLv3+
URL:            http://scidavis.sourceforge.net/
Source0:        http://sourceforge.net/projects/scidavis/files/SciDAVis/%{version}/%{name}-%{version}.tar.gz
# Patch to adjust qwt5-qt4 library path for Fedora
Patch0:         fix_qwt5_includes.patch
# Unbundle liborigin
Patch1:         unbundle_liborigin.patch
# Backport Fix http://sourceforge.net/p/scidavis/svn/1458/ 
Patch2:         fix_active_window.patch

# Doesn't build on arm right now
ExcludeArch:    %{arm}

BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gsl-devel
BuildRequires:  liborigin2-devel
BuildRequires:  muParser-devel
BuildRequires:  PyQt4-devel
BuildRequires:  python2-devel
BuildRequires:  qt-assistant-adp-devel
BuildRequires:  qt-devel
BuildRequires:  qwt5-qt4-devel
BuildRequires:  qwtplot3d-qt4-devel
BuildRequires:  sip-devel
BuildRequires:  zlib-devel
Requires:       gtk2
Requires:       PyQt4       

%description
SciDAVis is a free interactive application aimed at data analysis and 
publication-quality plotting. It combines a shallow learning curve and
an intuitive, easy-to-use graphical user interface with powerful 
features such as scriptability and extensibility.

%prep
%setup -q
# Unbundle liborigin
rm -rf 3rdparty/liborigin
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

%build
%if 0%{?__isa_bits} == 64
%qmake_qt4 PRESET=linux_package libsuff="64"
%else
%qmake_qt4 PRESET=linux_package
%endif
make %{?_smp_mflags}


%install
make INSTALL_ROOT="%{buildroot}" install

# Copy translations into right place
install -d %{buildroot}%{_datadir}/%{name}/translations
install -D -pm 644 %{name}/translations/*.qm %{buildroot}%{_datadir}/%{name}/translations/
%find_lang %{name} --with-qt

# Plugins are unversioned .so files
cd %{buildroot}%{_libdir}/%{name}/plugins
for plugin in `ls *.so`
do 
    mv ${plugin}.%{pluginversion} ${plugin}
    rm -f ${plugin}.*
done

%{_fixperms} %{buildroot}/*


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
# check available in Makefile but doesn't do anything right now
#make check


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%doc CHANGES README
%license gpl.txt
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/mimelnk/application/x-sciprj.desktop
%{_datadir}/icons/hicolor/*/apps/scidavis.*
%{_datadir}/icons/locolor/*/apps/scidavis.*
%{_sysconfdir}/scidavisrc.py
# Don't package the compiled versions of the file as this is a config
%exclude %{_sysconfdir}/scidavisrc.pyc
%exclude %{_sysconfdir}/scidavisrc.pyo

%changelog
* Mon Nov 28 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.14
- Rebuild for Fedora
* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.D8-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159
* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.D8-11
- rebuild for Boost 1.58
* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.D8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.D8-9
- Rebuilt for GCC 5 C++11 ABI change
* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.D8-8
- Rebuild for boost 1.57.0
* Fri Jan 02 2015 Christian Dersch <lupinix@fedoraproject.org> - 1.D8-7
- added patch to fix http://sourceforge.net/p/scidavis/svn/1458/ 
* Sat Dec 20 2014 Christian Dersch <lupinix@fedoraproject.org> - 1.D8-6
- added missing find_lang macro
- adjusted condition for 32/64 bit decision
* Mon Dec 15 2014 Christian Dersch <lupinix@fedoraproject.org> - 1.D8-5
- added ExcludeArch for arm as scidavis doesn't build there
* Mon Dec 15 2014 Christian Dersch <lupinix@fedoraproject.org> - 1.D8-4
- fixed spec
- added post/postun scripts
- removed versioned .so files
- don't package compiled versions of scidavisrc.py config file
* Thu Aug  7 2014 Christian Dersch <lupinix@fedoraproject.org> - 1.D8-3
- fixed spec to be conform with guidelines
* Mon Aug  4 2014 Christian Dersch <lupinix@fedoraproject.org> - 1.D8-2
- fixed BuildRequires
* Mon Aug  4 2014 Christian Dersch <lupinix@fedoraproject.org> - 1.D8-1
- initial spec
- inspired by old scidavis spec http://pkgs.fedoraproject.org/cgit/scidavis.git/tree/scidavis.spec?h=f15 
