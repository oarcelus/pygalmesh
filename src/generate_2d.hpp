#ifndef GENERATE_2D_HPP
#define GENERATE_2D_HPP

#include <memory>
#include <vector>

namespace pygalmesh {

void
generate_2d(
  const std::vector<std::array<double, 2>> & points,
  const std::vector<std::array<int, 2>> & constraints
);

} // namespace pygalmesh

#endif // GENERATE_2D_HPP
