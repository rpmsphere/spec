%undefine _debugsource_packages

Name: lft
Summary: Layer Four Traceroute
License: VOSTROM Public License for Open Source
Version: 3.91
Release: 1
Source0: %{name}-%{version}.tar.gz
URL: https://pwhois.org/lft/
Group: Productivity/Networking/Other 
BuildRequires: libpcap-devel

%description
LFT, short for Layer Four Traceroute, is a sort of 'traceroute' that often works much faster (than the commonly-used Van Jacobson method) and goes through many configurations of packet-filters (firewalls). More importantly, LFT implements numerous other features including AS number lookups through several reliable sources, loose source routing, netblock name lookups, et al. What makes LFT unique? LFT is the all-in-one traceroute tool because it can launch a variety of different probes using ICMP, UDP, and TCP protocols, or the RFC1393 trace method. For example, rather than only launching UDP probes in an attempt to elicit ICMP "TTL exceeded" from hosts in the path, LFT can send TCP SYN or FIN probes to target arbitrary services. Then, LFT listens for "TTL exceeded" messages, TCP RST (reset), and various other interesting heuristics from firewalls or other gateways in the path. LFT also distinguishes between TCP-based protocols (source and destination), which make its statistics slightly more realistic, and gives a savvy user the ability to trace protocol routes, not just layer-3 (IP) hops. With LFT's verbose output, much can be discovered about a target network.
WhoB is a likable whois client (see whois(1)) designed to provide everything a network engineer needs to know about a routed IP address by typing one line and reading one line. But even so, it's worth typing a few more lines because WhoB can do lots of other cool things for you! It can display the origin-ASN based on the global routing table at that time (according to Prefix WhoIs, RIPE NCC, or Cymru), the 'origin' ASN registered in the RADB (IRR), the netname and orgname, etc. By querying pWhoIs, WhoB can even show you all prefixes being announced by a specific Origin-ASN. WhoB performs the lookups quickly, the output is easily parsed by automated programs, and it's included as part of the Layer Four Traceroute (LFT) software package. LFT uses WhoB as a framework (and you can too, quite easily--see whois.h). Recent LFT releases (as of version 2.5) include WhoB functionality through a standalone "whob" client/command placed in the LFT binary directory.
LFT and WhoB continue to evolve and provide more and more useful data to network engineers and to anyone else that cares how IP datagrams are being routed. With the advent of smarter firewalls, traffic engineering, QoS, and per-protocol packet forwarding, LFT and WhoB have become invaluable tools for many network managers worldwide. 

%prep
%setup -q

%build
cp -f /usr/share/automake-*/config.guess config/
CFLAGS="$RPM_OPT_FLAGS -Wno-format-security -fPIC"
./configure --prefix=%{_prefix} --bindir=%{_sbindir} --mandir=%{_mandir}
#--build=x86_64
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc CHANGELOG COPYING README INSTALL TODO
%{_sbindir}/lft
%{_sbindir}/whob
%{_datadir}/man/man8/lft.8.*
%{_datadir}/man/man8/whob.8.*

%clean
%__rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 3.91
- Rebuilt for Fedora
* Mon Dec 14 2009 admin@eregion.de
- initial package
