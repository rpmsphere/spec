Summary:        Program for viewing and analyzing medical image data sets
Name:           amide
Version:        1.0.5git
Release:        1
License:        GPLv2+
Group:          Graphics
URL:            https://amide.sourceforge.net
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
BuildRequires:  intltool
BuildRequires:  perl-XML-Parser
BuildRequires:  dcmtk-devel
#BuildRequires: ffmpeg-devel
BuildRequires:  volpack-devel
BuildRequires:  xmedcon-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gnome-vfs-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libgnomecanvas-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  w3m udisks2
BuildRequires:  python2

%description
AMIDE is a tool for viewing and analyzing medical image data sets.
It's capabilities include the simultaneous handling of multiple data
sets imported from a variety of file formats, image fusion, 3D region
of interest drawing and analysis, volume rendering, and rigid body
alignments.

%prep
%setup -q
#sed -i 's|isinf(incremental_mi)|(isinf(incremental_mi))|' src/alignment_mutual_information.c
#sed -i '/gsl_multifit_covar (solver->J, 0.0, covar);/d' src/tb_profile.c

%build
LDFLAGS=-Wl,--allow-multiple-definition
autoreconf -ifv
%configure \
        --enable-libgsl=yes \
        --enable-libecat=no \
        --enable-amide-debug=no \
        --disable-scrollkeeper
# paralel build don't work on abf 
make

%install
%makeinstall

desktop-file-install --vendor "" --delete-original \
        --dir %{buildroot}%{_datadir}/applications \
        --add-category X-Red-Hat-Extra \
        %{buildroot}%{_datadir}/applications/*

rm -rf %{buildroot}/var/scrollkeeper

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README todo
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/gnome/*
%{_datadir}/omf/*
%{_datadir}/applications/*
%{_mandir}/man1/*

%changelog
* Tue Sep 24 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.5git
- Rebuilt for Fedora
* Tue Mar 17 2015 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1.0.5-3
+ Revision: 09d3434
- Bump release
