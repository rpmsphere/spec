Name:          pmidi
Version:       1.7.0
Release:       4.1
Summary:       A command line program to play midi files through the ALSA sequencer
Group:         Applications/Multimedia
URL:           http://www.parabola.me.uk/alsa/pmidi.html
Source:        http://download.sourceforge.net/sourceforge/pmidi/pmidi-%{version}.tar.gz
License:       GPLv2
BuildRequires: alsa-lib-devel

%description
The pmidi program is a straightforward command line program to play midi files
through the ALSA sequencer. As you can specify the client and port to connect
to on the command line it is also useful for testing ALSA or clients that need
to receive sequencer events.

%prep
%setup -q

%build
%configure
make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%doc AUTHORS COPYING ChangeLog NEWS README

%changelog
* Fri Nov 07 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7.0
- Rebuild for Fedora
* Fri Dec 13 2013 sr@parabola.me.uk
- Completely simplify the spec file
- Remove irrelevant info from description
* Fri Jul 10 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 1.6.0-2mamba
- specfile updated and rebuilt
* Sun Jan 08 2006 Silvan Calarco <silvan.calarco@qilinux.it> 1.6.0-1qilnx
- package created by autospec
