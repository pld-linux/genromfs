Summary:	Utility for creating romfs filesystems
Summary(pl):	Narzêdzie do tworzenia systemów plików romfs
Name:		genromfs
Version:	0.5.1
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/romfs/%{name}-%{version}.tar.gz
# Source0-md5:	fee69ecbf8f990fdb0ca0c7267c13e7e
Patch0:		%{name}-ac_am.patch
URL:		http://romfs.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveOS:	Linux

%define		_sbindir	/sbin

%description
genromfs is a tool for creating romfs filesystems, which are
lightweight, read-only filesystems supported by the Linux kernel.
Romfs filesystems are mainly used for the initial RAM disks used
during installation.

%description -l pl
genromfs jest narzêdziem s³u¿±cym do tworzenia systemów plików romfs,
które s± lekkimi systemami plików tylko do odczytu, obs³ugiwanymi
przez j±dro Linuksa. Romfs jest g³ównie u¿ywany na inicjalnym
ramdysku, u¿ywanym w trakcie startu systemu.

%prep
%setup -q
%patch -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog genromfs.lsm romfs.txt NEWS
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
