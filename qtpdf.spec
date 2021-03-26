%define git 20170626

Name: qtpdf
Version: 0.%{?git}
Source0: %{name}-%{git}.tar.xz
Source1: pdfium-%{git}.tar.xz
Release: 1
Summary: Qt library for PDF rendering
URL: https://github.com/qt-labs/qtpdf
License: LGPLv3
Group: System/Libraries
BuildRequires: qt5-qtbase-devel
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: python3-devel

%description
Qt library for PDF rendering

%package devel
Summary: Development files for %{name}
Group: Development/C
Requires: %{name}

%description devel
Development files (Headers etc.) for %{name},
a Qt library for PDF rendering.

%prep
%setup -qn %{name}-%{git} -a 1
%{_libdir}/qt5/bin/syncqt.pl -version `pkg-config --modversion Qt5Core`
2to3 -w src/3rdparty/gyp2pri.py

%build
qmake-qt5
make
cd examples/pdf/pdfviewer
qmake-qt5
make

%install
%makeinstall INSTALL_ROOT=%{buildroot}
cd examples/pdf/pdfviewer
%makeinstall INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_bindir}
mv pdfviewer %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
cat >%{buildroot}%{_datadir}/applications/%{name}.pdfviewer.desktop <<'EOF'
[Desktop Entry]
Type=Application
Terminal=false
Name=QtPDF
GenericName=PDF document viewer
Comment=A PDF document viewer using QtPDF
Categories=Viewer;Office;
Keywords=viewer;document;presentation;pdf;
Exec=qtpdf %F
MimeType=application/pdf;application/x-pdf;text/pdf;text/x-pdf;image/pdf;image/x-pdf;
EOF
chmod +x %{buildroot}%{_datadir}/applications/*.desktop

%files
%{_bindir}/*
%{_datadir}/applications/%{name}.pdfviewer.desktop
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.prl
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/Qt5Pdf
#{_libdir}/qt5/mkspecs/modules/*.pri
%{_libdir}/qt5/examples/pdf
%exclude %{_libdir}/libQt5Pdf.la

%changelog
* Mon May 18 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20170626
- Rebuild for Fedora
