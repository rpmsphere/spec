Name:           g3dviewer
Version:        0.2.99.4
Release:        6.1
Summary:        A 3D file/object viewer

Group:          Applications/Engineering
License:        GPLv2+
URL:            http://automagically.de/g3dviewer/
Source0:        http://automagically.de/files/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  libpng-devel
BuildRequires:  gtk2-devel
BuildRequires:  libglade2-devel
BuildRequires:  gtkglext-devel
BuildRequires:  libg3d-devel

BuildRequires:  gettext
BuildRequires:  desktop-file-utils

%description
G3DViewer is a 3D file viewer for GTK+ supporting a variety of file types:

* 3D Studio (.3ds, .prj)
* LightWave (.lw, .lwb, .lwo)
* Alias Wavefront (.obj)
* Impulse TurboSilver / Imagine (.iob)
* AutoCAD (.dxf)
* Quake II Models (.md2)
* Quake III Models (.md3)
* Neutral File Format (.nff)
* 3D Metafile (.3dmf, .3mf, .b3d)
* Caligari TrueSpace Objects (.cob)
* Quick3D Objects & Scenes (.q3o, q3s)
* VRML 1.0 files (.wrl, .vrml)
* AC3D objects (.ac, .acc)
* LeoCAD Models (.lcd)
* Racer car models (.ar, .dof)
* Ultimate Stunts car models (.glb)
* VDrift car models (.joe, .car)
* COLLADA & G**gle Earth (.dae, .kmz)
* LDraw (.dat, .mpd)
* ASCII Scene Exporter (.ase)

%prep
%setup -q

%build
export LDFLAGS="-lX11 -lm"
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
cp -p $RPM_BUILD_ROOT%{_datadir}/%{name}/glade/g3d48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPY* NEWS READ* TODO
%{_mandir}/man*/%{name}.*
%{_bindir}/g3d*
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.99.4
- Rebuild for Fedora

* Tue Feb 03 2009 Fabian Affolter <fabian@bernewireless.net> - 0.2.99.4-1
- Initial package for Fedora
