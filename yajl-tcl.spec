%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          yajl-tcl
Summary:       Tcl bindings for Yet Another JSON Library
Version:       1.6.2
Release:       0
License:       BSD-3-Clause
Group:         Development/Libraries/Tcl
Source:        %{name}-%{version}.tar.gz
URL:           https://github.com/flightaware/yajl-tcl
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.4
BuildRequires: libyajl-devel
Requires:      tcl >= 8.4
Requires:      libyajl2
BuildRoot:     %{buildroot}

%description
This is yajl-tcl, a direct Tcl interface to the yajl JSON generator library.

%prep
%setup -q -n %{name}-%{version}

%build
%{__autoconf}
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib} \
%ifarch x86_64
	--enable-64bit=yes \
%endif
	--with-tcl=%{directory}/%{_lib}
make

%install
make DESTDIR=%{buildroot} pkglibdir=%tcl_archdir/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README.md
%tcl_archdir/%{name}%{version}

%changelog

